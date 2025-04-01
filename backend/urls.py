from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

urlpatterns = [
    # Test method in order to check if api works.
    path('test/', api_test),

    # User methods.
    path('signup/', api_signup),
    path('login/', api_login),

    # Notes methods.
    path('save/', api_save_note),
    path('delete/',  api_delete_note),
    path('get/', api_get_notes),

    # LLM methods.
    path('ask/', api_ask),
]