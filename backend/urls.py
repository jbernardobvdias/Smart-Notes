from django.urls import path
from .views import api_test

urlpatterns = [
    path('test/', api_test),
]