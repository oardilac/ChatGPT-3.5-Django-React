from django.urls import path
from .views import upload_file, store_texto, serve_user_ui, get_texto
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', upload_file.as_view()),
    path('text/', store_texto.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)