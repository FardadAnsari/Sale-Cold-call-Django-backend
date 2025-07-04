# AiAssisstanceApp/transcription/urls.py

from django.urls import path
from .views import UploadAudioView, TranscriptionResultView
from .api_views import UploadAudioAPIView

urlpatterns = [
    path('upload/', UploadAudioView.as_view(), name='upload-audio'),           # Web-based form
    path('api/upload/', UploadAudioAPIView.as_view(), name='upload-audio-api'),# Swagger/API
    path('result/<int:recording_id>/', TranscriptionResultView.as_view(), name='transcription-result'),
]