from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def chat(request):
    return render(request, 'chat.html')

def notes(request):
    return render(request, 'notes.html')