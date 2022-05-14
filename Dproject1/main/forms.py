from django import forms
from .models import Post, Comment


class postForm(forms.ModelForm):
    class Meta:
        model = Post
        #fields = "__all__"
        fields = ('title', 'upload_time', 'contents',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('post', 'user',)
