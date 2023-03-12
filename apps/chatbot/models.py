from django.db import models
from django.utils import timezone
import openai
import redis
import json

# Create your models here.
API_KEY = ""
openai.api_key = API_KEY

# Connect to the Redis server
redis_client = redis.Redis(host='localhost', port=6379, db=0)

# model AIPost
class AIPost(models.Model):
    # id is default PK
    title = models.CharField(max_length=200, default="Title")
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    @property
    def summary(self):
        # Check if the summary is in the cache
        cache_key = f"summary:{self.pk}"
        summary = redis_client.get(cache_key)
        if summary:
            return json.loads(summary)

        text = self.text
        response_1 = openai.Completion.create(
                model="gpt-3.5-turbo",
                prompt=f"Summarize this into 5 sentences: {text}",
                temperature=0.7,
                max_tokens=256,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
        )
        summary = response_1["choices"][0]["text"]

        # Store the summary in the cache
        redis_client.set(cache_key, json.dumps(summary))
        return summary

    @property
    def question(self):
        # Check if the questions are in the cache
        cache_key = f"question:{self.pk}"
        question = redis_client.get(cache_key)
        if question:
            return json.loads(question)

        response_1 = self.summary
        response_2 = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=f"Create a study question from this text: {response_1}",
            temperature=0.6,
            max_tokens=150,
            top_p=1.0,
            frequency_penalty=0.3,
            presence_penalty=0.0
        )

        question = response_2["choices"][0]["text"]

        # Store the questions in the cache
        redis_client.set(cache_key, json.dumps(question))
        return question

class Answer(models.Model):
    post = models.ForeignKey(AIPost, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)

    @property
    def correctness(self):
        post = self.post
        text = self.text
        question = post.question
        # Check if the correctness assessment is in the cache
        cache_key = f"correctness:{self.pk}:{text}"
        correctness = redis_client.get(cache_key)
        if correctness:
            return json.loads(correctness)

        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt = f"Is this the correct answer to the question? \n Question: {question} \n Answer: {text}",
            temperature=0.6,
            max_tokens=150,
            top_p=1.0,
            frequency_penalty=0.3,
            presence_penalty=0.0
        )

        correctness = response["choices"][0]["text"]
        # Store the correctness assessment in the cache
        redis_client.set(cache_key, json.dumps(correctness))
        
        return correctness