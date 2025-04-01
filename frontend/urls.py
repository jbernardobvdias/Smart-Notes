from django.urls import path
from .views import *

urlpatterns = [
    # Always go to login then check if user is logged in.
    path('', login, name='login'),
    path('signup/', signup, name='signup'),
    path('app/', app, name='app'),
]