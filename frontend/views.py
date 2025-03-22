from django.shortcuts import render

def index(request):
    return render(request, 'templates/index.html')

def chat(request):
    return render(request, 'templates/chat.html')

def notes(request):
    return render(request, 'templates/notes.html')