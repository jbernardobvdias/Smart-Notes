from django.shortcuts import render
from django.http import JsonResponse
from backend.data.db import *
from backend.data.ollama import *

def api_test(request):
    return JsonResponse({"message": "Backend is working"})

def api_save_note(request):
    return add_note(request['title'], request['content'])

def api_delete_note(request):
    return delete_note(request['id'])

def api_get_notes(request):
    return get_notes()

def api_ask(request):
    return ask_ollama(request['question'])