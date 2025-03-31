from django.urls import path
from .views import *

urlpatterns = [
    path('test/', api_test),

    path('signup/', api_signup),
    path('login/', api_login),

    path('save/', api_save_note),
    path('delete/', api_delete_note),
    path('get/', api_get_notes),
    path('ask/', api_ask),
]