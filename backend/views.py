from django.shortcuts import render
from django.http import JsonResponse

def api_test(request):
    return JsonResponse({"message": "Backend is working"})

def api_save_note(request):
    return JsonResponse({"message": "Backend is working"})

def api_delete_note(request):
    return JsonResponse({"message": "Backend is working"})

def api_ask(request):
    return JsonResponse({"message": "Backend is working"})