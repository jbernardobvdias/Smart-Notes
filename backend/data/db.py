import os
import django
from backend.models import *

def add_note(title, content):
    note = Note(title=title, content=content)
    note.save()
    return True

def delete_note(id):
    note = Note.objects.get(id)
    note.delete()
    return True

def get_notes():
    all_notes = list(Note.objects.all())
    return all_notes

def sign_up(username, password):
    user = User(username=username, password=password)
    user.save()
    return True

def log_in(username, password):
    try:
        user = User.objects.get(username=username)
        if user.password == password:
            return True
    except User.DoesNotExist:
        return False
    
