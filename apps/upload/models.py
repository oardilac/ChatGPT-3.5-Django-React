from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)

class Chatbot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chatbots')
    chatbot_name = models.CharField(max_length=200)
    state_deployed = models.CharField(max_length=200)
    active_state = models.BooleanField(default=False)

    def __str__(self):
        return self.chatbot_name

class BaseFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='basefiles')
    chatbot = models.ForeignKey(Chatbot, on_delete=models.CASCADE, related_name='basefiles')
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='texts')
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    chatbot = models.ForeignKey(Chatbot, on_delete=models.CASCADE, related_name='texts')

    def __str__(self):
        return f'{self.fname} {self.lname}'

class Url(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='urls')
    chatbot = models.ForeignKey(Chatbot, on_delete=models.CASCADE, related_name='urls')
    url = models.URLField(max_length=200)