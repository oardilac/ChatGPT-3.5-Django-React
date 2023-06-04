from django.db import models

class BaseFile(models.Model):
    filename = models.CharField(max_length=255)
    location = models.URLField(max_length=200)
    file_type = models.CharField(max_length=50)
    file_size = models.IntegerField()
    file_encoding = models.CharField(max_length=50)
    modification_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class File(BaseFile):
    pass

class TextFile(BaseFile):
    tokens = models.IntegerField()
    characters = models.IntegerField()