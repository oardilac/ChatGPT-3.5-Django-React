from rest_framework import generics
from rest_framework.response import Response
from .models import AIPost, Answer
from .serializers import AIPostSerializer, AnswerSerializer

class AIPostList(generics.ListCreateAPIView):
    queryset = AIPost.objects.all()
    serializer_class = AIPostSerializer

class AIPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AIPost.objects.all()
    serializer_class = AIPostSerializer

class AnswerList(generics.ListCreateAPIView):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        queryset = Answer.objects.all()
        post_id = self.request.query_params.get('post_id', None)
        if post_id is not None:
            queryset = queryset.filter(post=post_id)
        return queryset

class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
