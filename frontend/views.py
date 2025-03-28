from django.shortcuts import render
from django.urls import reverse

def index(request):
    return render(request, 'pages/index.html', {'index_url': reverse('index')})

def notes(request):
    return render(request, 'pages/notes.html', {'index_url': reverse('notes')})

def chat(request):
    return render(request, 'pages/chat.html', {'index_url': reverse('chat')})