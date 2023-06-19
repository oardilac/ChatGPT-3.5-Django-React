from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import status
from .models import User, Chatbot, SubmitFiles, RequestModelTexto, Url
from .serializers import UserSerializer, ChatbotSerializer, SubmitFilesSerializer, RequestModelTextoSerializer, UrlSerializer
from google.cloud import firestore, storage
from firebase_admin import credentials
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from urllib.parse import quote
from django.http import JsonResponse
import os
import chardet
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import tiktoken
import logging
from decouple import config
from django.db import transaction
from rest_framework.pagination import PageNumberPagination


logger = logging.getLogger(__name__)
cred = credentials.ApplicationDefault()
db = firestore.Client(project='chatmine-388722')

def get_storage_client():
    try:
        return storage.Client()
    except Exception as e:
        return None, str(e)
client = get_storage_client()
bucket_name = config("BUCKET_NAME", default=None)

# Defining the allowed extensions for files to be uploaded
ALLOWED_EXTENSIONS = ['.csv', '.txt', '.pdf', '.xlsx']

# Function to get the filename from a given url
def get_filename_from_url(url: str):
    return quote(url, safe='')

# This view handles the creation of a chatbot instance in the database
@method_decorator(csrf_exempt, name='dispatch')
class CreateChatbotView(APIView):

    @transaction.atomic
    def post(self, request):
        serializer = ChatbotSerializer(data=request.data)
        if serializer.is_valid():
            chatbot_name = serializer.validated_data['chatbot_name']
            state_deployed = serializer.validated_data['state_deployed']
            active_state = serializer.validated_data['active_state']
            
            doc_ref = db.collection('Chatbots').document()
            doc_ref.set({
                'chatbot_name': chatbot_name,
                'state_deployed': state_deployed,
                'active_state': active_state
            })

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# This view retrieves a document from the 'datafile' collection
@method_decorator(csrf_exempt, name='dispatch')
class DocumentView(APIView):

    def get(self, request, doc_id):
        doc_ref = db.collection('datafile').document(doc_id)
        try:
            doc = doc_ref.get()
            if doc.exists:
                return Response(doc.to_dict())
            else:
                return Response({"error": "Document not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.exception("Error while retrieving document: %s", e)
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# A custom pagination class for paginating the document list
class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10  # Default to 10 items per page
    page_size_query_param = 'page_size'  # Allow the client to override the page size

# This view retrieves a list of all documents in the 'datafile' collection
@method_decorator(csrf_exempt, name='dispatch')
class DocumentListView(APIView):
    # Use the custom pagination class
    pagination_class = CustomPageNumberPagination

    def get(self, request):
        try:
            # Get all documents, ordered by 'user_id'
            query = db.collection('datafile').order_by('user_id').stream()
            # Convert the query to a list of dictionaries
            data = [doc.to_dict() for doc in query]

            # Use the pagination class to paginate the data
            paginator = self.pagination_class()

            # If page_size parameter is provided in request, change the page size
            page_size = request.query_params.get(self.pagination_class.page_size_query_param)
            if page_size:
                paginator.page_size = int(page_size)

            paginated_data = paginator.paginate_queryset(data, request)

            return paginator.get_paginated_response(paginated_data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# This view handles the uploading of files
@method_decorator(csrf_exempt, name='dispatch')
class FileUploadView(APIView):

    @transaction.atomic
    def post(self, request, *args, **kwargs):     
        uploaded_files = request.FILES.getlist('files')
        bucket = client.get_bucket(bucket_name)

        if not uploaded_files:
            return Response({'files': ['No files to upload.']}, status=status.HTTP_400_BAD_REQUEST)

        results = []
        errors = []

        for file in uploaded_files:
            filename = os.path.basename(file.name)
            file_type = os.path.splitext(filename)[1]

            if file_type not in ALLOWED_EXTENSIONS:
                errors.append({
                    "filename": filename,
                    "error": f"El archivo no es uno de los solicitados: {', '.join(ALLOWED_EXTENSIONS)}"
                })
                continue

            try:
                contents = file.read()  # Read the file

                # If the file is empty, sets the content to an empty utf-8 string
                if len(contents) == 0:
                    errors.append({"filename": filename, "error": f"El archivo {file.name} se encuentra vacío"})
                    continue

                # Save the file to the bucket
                blob = bucket.blob(filename)
                blob.upload_from_string(contents)

                # Get the file metadata
                file_size = blob.size
                file_encoding = chardet.detect(contents)['encoding'] if file_type in ['csv', 'txt'] else 'binary'
                file_modification_time = blob.updated
                doc_ref = db.collection('datafile').document()
                doc_ref.set({
                    'filename': file.name,
                    'location': blob.public_url,
                    'file_type': file_type,
                    'file_size': file_size,
                    'file_encoding': file_encoding,
                    'file_modification_time': file_modification_time
                })
                # Creas el diccionario con los datos del archivo
                file_data = {
                    'filename': file.name,
                    'location': blob.public_url,
                    'file_type': file_type,
                    'file_size': file_size,
                    'file_encoding': file_encoding,
                }

                # Creas la instancia del serializer con los datos del archivo
                file_serializer = SubmitFilesSerializer(data=file_data)

                # Validas y guardas los datos
                if file_serializer.is_valid():
                    new_file = file_serializer.save()
                    results.append(new_file)
                else:
                    errors.append({"filename": filename, "error": f"Unexpected error occurred: {file_serializer.errors}"})

            except Exception as e:
                logger.exception("Error while uploading file: %s", e)
                errors.append({"filename": filename, "error": f"Unexpected error occurred: {str(e)}"})
        
        return JsonResponse({
            "uploaded": [SubmitFilesSerializer(file).data for file in results], 
            "errors": errors
        })


# This view handles the storage of text data
@method_decorator(csrf_exempt, name='dispatch')
class StoreTextoView(APIView):

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = RequestModelTextoSerializer(data=data)

        if serializer.is_valid():
            payload = RequestModelTexto(**data)

            fname = payload.fname
            lname = payload.lname
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")  # Generate a unique timestamp
            filename = f"data_{timestamp}.txt"  # Add a timestamp to the filename
            bucket = client.get_bucket(bucket_name)
            blob = bucket.blob(filename)

            file_type = 'txt'
            tt_encoding = tiktoken.encoding_for_model('gpt-4')
            tokens = tt_encoding.encode(lname)
            total_tokens = len(tokens)
            data = f'Nombre del chatbot: {fname}\nDato: {lname}\n'

            blob.upload_from_string(data, content_type='text/plain')  # Upload the data

            tokens = tt_encoding.encode(lname)
            total_tokens = len(tokens)
            character_count = len(lname)
            file_size = blob.size
            file_encoding = 'utf-8'
            file_modification_time = blob.updated

            doc_ref = db.collection('datafile').document()
            doc_ref.set({
                'filename': filename,
                'location': blob.public_url,
                'file_type': file_type,
                'file_size': file_size,
                'file_encoding': file_encoding,
                'file_modification_time': file_modification_time,
                'tokens': total_tokens,
                'characters': character_count
            })

            return JsonResponse({"file": 'Cargado exitoso'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# This view saves a URL in the database
@method_decorator(csrf_exempt, name='dispatch')
class SaveUrlView(APIView):

    @transaction.atomic
    def post(self, request):
        serializer = UrlSerializer(data=request.data)
        if serializer.is_valid():
            url = serializer.validated_data.get('url')
            if url is None:
                return Response({"error": "url fields are required"}, status=status.HTTP_400_BAD_REQUEST)

            try:
                response = requests.get(url)
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

            # Use BeautifulSoup to extract the text from the HTML
            soup = BeautifulSoup(response.content, 'html.parser')
            text = soup.get_text()

            # Prepare the data to be uploaded to Google Cloud Storage
            filename = get_filename_from_url(url)
            bucket = client.get_bucket(bucket_name)
            blob = bucket.blob(filename)
            
            blob.upload_from_string(text, content_type='text/plain')

            file_size = blob.size

            file_modification_time = blob.updated
            
            doc_ref = db.collection('datafile').document()
            doc_ref.set({
                'filename': filename,
                'location': url,
                'file_size': file_size,
                'file_modification_time': file_modification_time
            })

            return Response({"response": "Archivo guardado con éxito"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# This view scrapes a website's sitemap
@method_decorator(csrf_exempt, name='dispatch')
class ScrapeSitemapView(APIView):
    def post(self, request):
        serializer = UrlSerializer(data=request.data)
        if serializer.is_valid():
            url = serializer.validated_data.get('url')

            if url is None:
                return Response({"error": "url field is required"}, status=status.HTTP_400_BAD_REQUEST)

            try:
                response = requests.get(url)
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

            if url.endswith('.xml'):
                soup = BeautifulSoup(response.content, 'xml')
                tags = soup.find_all('loc')
            else:
                soup = BeautifulSoup(response.content, 'html.parser')
                tags = soup.find_all('a')

            urls = [tag.get('href') if not url.endswith('.xml') else tag.text for tag in tags]

            return Response({"urls": urls, "message": "Web scraping exitoso"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)