from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from google.cloud import storage
from google.auth import exceptions
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import os
import chardet
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
from .models import File, TextFile
import tiktoken
from django.shortcuts import render
from django.views import View

# Load environment variables
SERVICE_ACCOUNT_KEY_PATH = 'D:\Oliver\django\ChatGPT-3.5-Django-React\chatmine.json'
cred = credentials.Certificate(SERVICE_ACCOUNT_KEY_PATH)
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

def get_storage_client():
    try:
        return storage.Client.from_service_account_json(SERVICE_ACCOUNT_KEY_PATH)
    except exceptions.DefaultCredentialsError as e:
        return JsonResponse({"error": str(e)}, status=500)

class upload_file(View):

    def get(self, request):
        files = File.objects.all()
        return render(request, 'userUI.html', {'files': files})

    

    def post(self, request):
        client = get_storage_client()
        results = []
        errors = []
        bucket_name = "chatmine-388722"
        bucket = client.get_bucket(bucket_name)

        for file in request.FILES.getlist('files'):
            filename = os.path.basename(file.name)

            file_type = None
            if filename.endswith('.csv'):
                file_type = 'CSV'
            elif filename.endswith('.txt'):
                file_type = 'TXT'
            elif filename.endswith('.pdf'):
                file_type = 'PDF'
            
            if file_type is None:
                errors.append({"filename": filename, "error": "El archivo no es uno de los solicitados: CSV, TXT, PDF"})
                continue
            
            if file_type is None:
                errors.append({"filename": filename, "error": "El archivo no es uno de los solicitados: CSV, TXT, PDF"})
                continue
    
            try:
                contents = file.read()  # Read file
                
                # Check if file already exists in the bucket
                if storage.Blob(bucket=bucket, name=filename).exists(client):
                    errors.append({"filename": filename, "error": f"El archivo {file.name} ya existe en el bucket"})
                    continue

                # Save the file to the bucket
                blob = bucket.blob(filename)
                blob.upload_from_string(contents)

                # Get the file metadata
                file_size = blob.size
                file_encoding = chardet.detect(contents)['encoding'] if file_type in ['CSV', 'TXT'] else 'binary'
                file_modification_time = blob.updated

                doc_ref = db.collection('chatmine-388722').document()
                doc_ref.set({
                    'filename': filename,
                    'location': blob.public_url,
                    'file_type': file_type,
                    'file_size': file_size,
                    'file_encoding': file_encoding,
                    'modification_time': file_modification_time,
                })

                results.append(File(  # use your Django model for the response
                    filename=file.name,
                    location=blob.public_url,
                    file_type=file_type,
                    file_size=file_size,
                    file_encoding=file_encoding,
                    modification_time=file_modification_time
                ))
                
            except Exception as e:
                errors.append({"filename": filename, "error": str(e)})

        return JsonResponse({"uploaded": [file.to_json() for file in results], "errors": errors})
    

class store_texto(View):
    def get(self, request):
        files = TextFile.objects.all()
        return render(request, 'texto.html', {'files': files})

    
    def post(self, request):
        client = get_storage_client()
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")  # Generates a unique timestamp
        filename = f"data_{timestamp}.txt"  # Add the timestamp to the filename

        bucket_name = "chatmine-388722"
        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob(filename)

        file_type = 'TXT'
        tt_encoding = tiktoken.encoding_for_model('gpt-4')
        data = f'Nombre del chatbot: {fname}\nDato: {lname}\n'

        blob.upload_from_string(data, content_type='text/plain')  # Upload the data

        tokens = tt_encoding.encode(lname)
        total_tokens = len(tokens)
        character_count = len(lname)
        file_size = blob.size
        file_encoding = 'utf-8'
        file_modification_time = datetime.now()

        doc_ref = db.collection('chatmine-388722').document()
        doc_ref.set({
            'filename': filename,
            'location': blob.public_url,
            'file_type': file_type,
            'file_size': file_size,
            'file_encoding': file_encoding,
            'modification_time': file_modification_time,
            'tokens': total_tokens,
            'characters': character_count
        })

        return JsonResponse({"file": 'Cargado exitoso'})

@csrf_exempt
def serve_user_ui(request):
    pass


@csrf_exempt
def get_texto(request):
    pass