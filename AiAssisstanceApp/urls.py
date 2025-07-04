# AiAssisstanceApp/urls.py

from django.urls import path, include
from AiAssisstanceApp.transcription.api_views import UploadAudioAPIView

urlpatterns = [
    path("transcription/", include("AiAssisstanceApp.transcription.urls")),
     path("transcription/upload/", UploadAudioAPIView.as_view(), name="upload-audio-api"),
]