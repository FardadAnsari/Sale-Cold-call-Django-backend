from django.urls import path
from .views import UploadAudioView, TranscriptionStatusView

urlpatterns = [
    path('upload/', UploadAudioView.as_view(), name='upload-audio'),
    path('status/<str:recording_id>/', TranscriptionStatusView.as_view(), name='transcription-status'),
]