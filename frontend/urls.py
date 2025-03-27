from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('notes/', notes, name='notes'),
    path('chat/', chat, name='chat'),
]