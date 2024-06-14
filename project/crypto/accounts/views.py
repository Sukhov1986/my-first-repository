from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


def register(request):
    if request.method == "GET":
        return render(request, 'accounts/register.html',
                      {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('profile')
            except IntegrityError:
                return render(request, 'accounts/register.html', {'form': UserCreationForm,
                                                                  'error': "Такое имя пользователя уже существует"})
        else:
            return render(request, 'accounts/register.html', {'form': UserCreationForm,
                                                              'error': "Пароли не совпадают"})


def profile(request):
    return render(request, 'accounts/profile.html')


def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('index')


def loginuser(request):
    if request.method == "GET":
        return render(request, 'accounts/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'accounts/loginuser.html', {'form': AuthenticationForm(),
                                                               'error': 'Неверные данные для входа'})
        else:
            login(request, user)
            return redirect('profile')
