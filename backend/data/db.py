import os
import django
from models import Note

def add_note(title, content):
    note = Note(title=title, content=content)
    note.save()

def delete_note(id):
    note = Note.objects.get(id)
    note.delete()

def get_notes():
    all_notes = list(Note.objects.all())
    return all_notes