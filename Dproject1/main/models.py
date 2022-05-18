from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, default="", null=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default="", null=True)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='like_post')
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
