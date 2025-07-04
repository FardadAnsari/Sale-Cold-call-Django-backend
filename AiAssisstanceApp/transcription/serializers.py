from rest_framework import serializers
from AiAssisstanceApp.models import CallRecording

class CallRecordingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallRecording
        fields = ['id', 'audio_file', 'transcribed_text', 'gemini_feedback']