from chatbot.models import Chat
from django.apps import AppConfig
from django.conf import settings


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

def chats(request):
    chats = Chat.objects.all().order_by('-created_at')
    return {'chats': chats}

def chatbot_settings(request):
    """
    Add settings to the context that are needed by the chatbot.
    """
    return {
        'CHATBOT_OPENAI_API_KEY': settings.CHATBOT_OPENAI_API_KEY,
        'CHATBOT_OPENAI_MODEL': settings.CHATBOT_OPENAI_MODEL,
        'CHATBOT_MAX_HISTORY': settings.CHATBOT_MAX_HISTORY,
        'CHATBOT_MAX_RESPONSE_LENGTH': settings.CHATBOT_MAX_RESPONSE_LENGTH,
        'CHATBOT_MIN_CONFIDENCE': settings.CHATBOT_MIN_CONFIDENCE,
    }