from django.urls import path
from .views import (
    CreateChatbotView,
    DocumentView,
    DocumentListView,
    FileUploadView,
    StoreTextoView,
    SaveUrlView,
    ScrapeSitemapView,
)
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('chatbots/', CreateChatbotView.as_view(), name='chatbot'),
    path('documents/<str:doc_id>/', DocumentView.as_view(), name='document'),
    path('documents/', DocumentListView.as_view(), name='documents'),
    path('uploadfiles/', FileUploadView.as_view(), name='uploadfiles'),
    path('storetexto/', StoreTextoView.as_view(), name='storetexto'),
    path('saveurl/', SaveUrlView.as_view(), name='saveurl'),
    path('scrapesitemap/', ScrapeSitemapView.as_view(), name='scrapesitemap'),
]

urlpatterns = format_suffix_patterns(urlpatterns)