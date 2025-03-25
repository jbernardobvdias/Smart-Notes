from django.shortcuts import render
from django.http import JsonResponse
from data import db, ollama

def api_test(request):
    return JsonResponse({"message": "Backend is working"})

def api_save_note(request):
    return db.add_note(request['title'], request['content'])

def api_delete_note(request):
    return db.delete_note(request['id'])

def api_get_notes(request):
    return db.get_notes()

def api_ask(request):
    return ollama.ask_ollama(request['question'])