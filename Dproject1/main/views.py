from multiprocessing import context
from django.shortcuts import get_object_or_404, render, redirect, HttpResponseRedirect
from django.utils import timezone

# Create your views here.
from main.models import Post
from .forms import postForm

def index(request):
    posts = Post.objects.filter(upload_time__lte=timezone.now()).order_by('upload_time')
    return render(request, 'index.html', {'posts':posts})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'detail.html', {'post':post})

def create(request):
    context = {}
    form = postForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            post = form.save()
            return redirect('detail', post.pk)
    else:
        context['form'] = form
        return render(request, "create.html", context)

def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('index')

def update(request, pk):
    context = {}
    post = get_object_or_404(Post, pk=pk)

    form = postForm(request.POST or None, instance = post)

    if form.is_valid():
        form.save()
        return redirect('detail', post.pk)
    
    context["form"] = form
    return render(request, "update.html", context)
