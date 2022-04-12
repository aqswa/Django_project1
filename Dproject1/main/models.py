from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    upload_time=models.DateTimeField(default=datetime.now())
    contents = models.TextField()
    
    def __str__(self):
        return self.title
