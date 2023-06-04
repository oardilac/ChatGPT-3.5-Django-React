from django.db import models

class File(models.Model):
    filename = models.CharField(max_length=255)
    location = models.URLField(max_length=200)
    file_type = models.CharField(max_length=50)
    file_size = models.IntegerField()
    file_encoding = models.CharField(max_length=50)
    modification_time = models.DateTimeField(auto_now=True)

    def to_json(self):
        return{
            'filename': self.filename,
            'location': self.location,
            'file_type': self.file_type,
            'file_syze': self.file_size,
            'file_encoding': self.file_encoding,
            'modification_time': self.modification_time
        }
    

class TextFile(models.Model):
    filename = models.CharField(max_length=255)
    location = models.URLField(max_length=200)
    file_type = models.CharField(max_length=50)
    file_size = models.IntegerField()
    file_encoding = models.CharField(max_length=50)
    modification_time = models.DateTimeField(auto_now=True)
    tokens = models.IntegerField()
    characters = models.IntegerField()

    def to_json(self):
        return{
            'filename': self.filename,
            'location': self.location,
            'file_type': self.file_type,
            'file_syze': self.file_size,
            'file_encoding': self.file_encoding,
            'modification_time': self.modification_time,
            'tokens': self.tokens,
            'characters': self.characters
        }