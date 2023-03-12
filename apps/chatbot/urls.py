from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('posts/', views.AIPostList.as_view()),
    path('posts/<int:pk>/', views.AIPostDetail.as_view()),
    path('posts/<int:pk>/answers/', views.AnswerList.as_view()),
    path('posts/<int:pk>/answers/<int:answer_pk>/', views.AnswerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
