from django.shortcuts import get_object_or_404, render
from django.utils import timezone

# Create your views here.
from main.models import Post

def index(request):
    posts = Post.objects.filter(upload_time__lte=timezone.now()).order_by('upload_time')
    return render(request, 'index.html', {'posts':posts})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'detail.html', {'post':post})