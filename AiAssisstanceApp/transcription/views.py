from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
import threading
from AiAssisstanceApp.models import CallRecording
from AiAssisstanceApp.transcription.worker import run_transcription
from AiAssisstanceApp.transcription.serializers import CallRecordingSerializer
from drf_spectacular.utils import extend_schema, OpenApiTypes, OpenApiParameter
from rest_framework import status
from AiAssisstanceApp.models import AgentCallTranscript

@extend_schema(
    request={
        'multipart/form-data': {
            'type': 'object',
            'properties': {
                'audio_file': {
                    'type': 'string',
                    'format': 'binary',
                    'description': 'Upload audio file',
                },
            },
            'required': ['audio_file'],
        }
    },
    responses={200: OpenApiTypes.STR},
)
class UploadAudioView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        audio_file = request.FILES.get('audio_file')
        
        ...
        return Response({'message': 'File uploaded and transcription started.'})
class TranscriptionStatusView(APIView):
    def get(self, request, recording_id):
        try:
            transcript_entry = AgentCallTranscript.objects.get(agent_id=recording_id)
            return Response({
                "status": "completed",
                "transcript": transcript_entry.transcript,
                "summary": transcript_entry.summary,
                "feedback": transcript_entry.feedback,
                "score": transcript_entry.score
            })
        except AgentCallTranscript.DoesNotExist:
            return Response({"status": "processing"}, status=status.HTTP_202_ACCEPTED)