from django.urls import path
from .api_views import UploadAudioAPIView, TranscriptionResultAPIView

urlpatterns = [
    path('upload/', UploadAudioAPIView.as_view(), name='upload-audio-api'),
    path('result/<int:recording_id>/', TranscriptionResultAPIView.as_view(), name='transcription-result-api'),
]