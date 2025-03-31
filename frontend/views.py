from django.shortcuts import render
from django.urls import reverse

def index(request):
    return render(request, 'pages/index.html', {'index_url': reverse('index')})

def app(request):
    return render(request, 'pages/app.html', {'index_url': reverse('app')})