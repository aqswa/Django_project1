from django.shortcuts import get_object_or_404, render, redirect, HttpResponseRedirect
from django.utils import timezone

# Create your views here.
from main.models import Post, Comment
from .forms import CommentForm, postForm


def index(request):
    posts = Post.objects.filter(
        upload_time__lte=timezone.now()).order_by('upload_time')
    return render(request, 'index.html', {'posts': posts})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment_form = CommentForm
    return render(request, 'detail.html', {'post': post, 'comment_form': comment_form})


def create(request):
    context = {}
    form = postForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('detail', post.pk)
    else:
        context['form'] = form
        return render(request, "create.html", context)


def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user.authenticated:
        if request.user == post.user:
            post.delete()
            return redirect('index')
    return redirect('detail', post.pk)


def update(request, pk):
    context = {}
    post = get_object_or_404(Post, pk=pk)

    if request.user == post.user:
        if request.method == 'POST':
            form = postForm(request.POST or None, instance=post)
            if form.is_valid():
                form.save()
                return redirect('detail', post.pk)
        else:
            form = postForm(instance=post)
    else:
        return redirect('index')

    context = {
        'form': form,
        'post': post,
    }
    return render(request, "update.html", context)


def comment_create(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
        return redirect('detail', pk)
    return redirect('common:login')


def comment_delete(request, post_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('detail', post_pk)
