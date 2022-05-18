from django import forms
from .models import Post, Comment, Category

choices = Category.objects.all().values_list('name', 'name')
choice_list = []

for item in choices:
    choice_list.append(item)


class postForm(forms.ModelForm):
    class Meta:
        model = Post
        #fields = "__all__"
        fields = ('title', 'upload_time', 'category', 'contents',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('post', 'user',)
