from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, default="", null=True)
    title = models.CharField(max_length=100)
    upload_time = models.DateTimeField(default=timezone.now)
    contents = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, default="", null=True)
    comment_text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def approve(self):
        self.save()

    def __str__(self):
        return self.comment_text
