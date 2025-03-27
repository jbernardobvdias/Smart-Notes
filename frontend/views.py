from django.shortcuts import render
from django.urls import reverse

def index(request):
    return render(request, 'index.html', {'index_url': reverse('index')})

def notes(request):
    return render(request, 'notes.html', {'index_url': reverse('notes')})

def chat(request):
    return render(request, 'chat.html', {'index_url': reverse('chat')})