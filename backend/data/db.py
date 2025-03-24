import os
import django
from models import Notes

def add_note(title, content):
    note = Notes(title=title, content=content)
    note.save()
    print(f'Note "{title}" saved successfully.')

def get_notes():
    print("Test")