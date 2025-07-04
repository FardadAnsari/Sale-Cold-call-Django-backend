# AiAssisstanceApp/views.py
from django.http import HttpResponse
from django.urls import path

def home(request):
    return HttpResponse("Welcome to the Cold Call Transcription API!")

urlpatterns = [
    path('', home, name='home'),
]