from django.db import models

class Chatbot(models.Model):
    chatbot_name = models.CharField(max_length=200)
    state_deployed = models.CharField(max_length=200)
    active_state = models.BooleanField(default=False)

    def __str__(self):
        return self.chatbot_name

class BaseFile(models.Model):
    filename = models.CharField(max_length=255)
    location = models.URLField(max_length=200)
    file_type = models.CharField(max_length=50)
    file_size = models.IntegerField()
    file_encoding = models.CharField(max_length=50)
    modification_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.filename

class SubmitFiles(BaseFile):
    pass

class RequestModelTexto(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.fname} {self.lname}'

class Url(models.Model):
    url = models.URLField(max_length=200)