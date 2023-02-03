# Core Django
from django.urls import path, include

urlpatterns = [
    path('', include('forms.api.router')),
]
