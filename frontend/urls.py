from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('chat/', chat, name='chat'),
    path('notes/', notes, name='notes'),
]