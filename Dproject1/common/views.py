from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

# Create your views here.


def login(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('index')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, "login.html", context)


def signup(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('index')


def update(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'account_update.html', context)


def delete(request):
    if request.user.is_authenticated:
        request.user.delete()  # 유저 정보 제거
        auth_logout(request)  # 세션 제거
    return redirect('index')
