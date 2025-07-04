# AiAssisstanceApp/urls.py

from django.urls import path, include

urlpatterns = [
    path("transcription/", include("AiAssisstanceApp.transcription.urls")),
]