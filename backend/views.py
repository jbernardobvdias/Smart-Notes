from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from backend.data.db import add_note, delete_note, get_notes
from backend.data.ollama import ask_ollama

def api_test(request):
    return JsonResponse({"message": "Backend is working"})

@csrf_exempt
def api_signup(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request method"}, status=400)
    try:
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        email = data.get("email", "")
        if not username or not password:
            return JsonResponse({"error": "Username and password are required."}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username already exists."}, status=400)
        
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        return JsonResponse({"message": "User created successfully."})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def api_login(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request method"}, status=400)
    try:
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        if not username or not password:
            return JsonResponse({"error": "Username and password are required."}, status=400)
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"message": "Logged in successfully."})
        else:
            return JsonResponse({"error": "Invalid credentials."}, status=401)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

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
