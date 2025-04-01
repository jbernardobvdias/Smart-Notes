from django.shortcuts import render
from django.urls import reverse

def login(request):
    return render(request, 'pages/login.html', {'index_url': reverse('login')})

def signup(request):
    return render(request, 'pages/signup.html', {'index_url': reverse('signup')})

def app(request):
    return render(request, 'pages/app.html', {'index_url': reverse('app')})