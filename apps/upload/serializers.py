from rest_framework import serializers
from .models import User, Chatbot, SubmitFiles, RequestModelTexto, Url

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id']

class ChatbotSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Chatbot
        fields = ['user', 'chatbot_name', 'state_deployed', 'active_state']

class SubmitFilesSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    chatbot = ChatbotSerializer(read_only=True)
    filename = serializers.CharField(max_length=255)
    file_type = serializers.ChoiceField(choices=['.csv', '.txt', '.pdf', '.xlsx'])

    class Meta:
        model = SubmitFiles
        fields = ['user', 'filename', 'location', 'file_type', 'file_size', 'file_encoding', 'modification_time']

class RequestModelTextoSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    chatbot = ChatbotSerializer(read_only=True)
    fname = serializers.CharField(max_length=100)
    lname = serializers.CharField(max_length=100)

    class Meta:
        model = RequestModelTexto
        fields = ['user', 'chatbot', 'fname', 'lname']

class UrlSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    chatbot = ChatbotSerializer(read_only=True)
    url = serializers.URLField(max_length=200)

    class Meta:
        model = Url
        fields = ['user', 'chatbot', 'url']