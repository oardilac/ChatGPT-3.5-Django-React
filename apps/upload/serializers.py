from rest_framework import serializers
from .models import Chatbot, SubmitFiles, RequestModelTexto, Url

class ChatbotSerializer(serializers.ModelSerializer):
    chatbot_name = serializers.CharField(max_length=200)
    state_deployed = serializers.CharField(max_length=200)
    active_state = serializers.BooleanField(default=False)

    class Meta:
        model = Chatbot
        fields = ['chatbot_name', 'state_deployed', 'active_state']

class SubmitFilesSerializer(serializers.Serializer):
    filename = serializers.CharField(max_length=255)
    file_type = serializers.ChoiceField(choices=['.csv', '.txt', '.pdf', '.xlsx'])
    location = serializers.URLField(max_length=200)
    file_size = serializers.IntegerField()
    file_encoding = serializers.CharField(max_length=50)
    modification_time = serializers.DateTimeField()


class RequestModelTextoSerializer(serializers.ModelSerializer):
    fname = serializers.CharField(max_length=100)
    lname = serializers.CharField(max_length=100)

    class Meta:
        model = RequestModelTexto
        fields = ['fname', 'lname']

class UrlSerializer(serializers.ModelSerializer):
    url = serializers.URLField(max_length=200)

    class Meta:
        model = Url
        fields = ['url']