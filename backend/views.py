from django.shortcuts import render
from django.http import JsonResponse
from backend.data.db import *
from backend.data.ollama import *
import json
from django.views.decorators.csrf import csrf_exempt

def api_test(request):
    return JsonResponse({"message": "Backend is working"})

@csrf_exempt
def api_signup(request):
    if request.method == "POST":
        data = json.loads(request.body)
        return JsonResponse({"result" : sign_up(data['username'], data['password'])}, status=200)
    return JsonResponse({"error": "Invalid request"}, status=400)

@csrf_exempt
def api_login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        return log_in(data['username'], data['password'])
    return JsonResponse({"error": "Invalid request"}, status=400)

def api_save_note(request):
    if request.method == "POST":
        data = json.loads(request.body)
        return add_note(data['title'], data['content'])
    return JsonResponse({"error": "Invalid request"}, status=400)

def api_delete_note(request):
    if request.method == "POST":
        data = json.loads(request.body)
        return delete_note(data['id'])
    return JsonResponse({"error": "Invalid request"}, status=400)

def api_get_notes(request):
    return get_notes()

def api_ask(request):
    if request.method == "POST":
        data = json.loads(request.body)
        return ask_ollama(data['question'])
    return JsonResponse({"error": "Invalid request"}, status=400)
