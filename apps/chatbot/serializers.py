from rest_framework import serializers
from .models import AIPost, Answer


class AIPostSerializer(serializers.ModelSerializer):
    # Use SerializerMethodField to add summary and question fields to the serializer
    summary = serializers.SerializerMethodField()
    question = serializers.SerializerMethodField()

    class Meta:
        model = AIPost
        fields = ['id', 'title', 'text', 'summary', 'question']
        read_only_fields = ('created_at', )

    def get_summary(self, obj):
        # Define the method to extract summary from the AIPost object
        return obj.generate_summary()

    def get_question(self, obj):
        # Define the method to extract question from the AIPost object
        return obj.generate_question()


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['id', 'post', 'correctness', 'answer']