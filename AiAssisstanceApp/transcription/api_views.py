from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from AiAssisstanceApp.models import CallRecording
from .transcriber import run_transcription
from drf_spectacular.utils import extend_schema, OpenApiTypes

class UploadAudioAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    @extend_schema(
        request={"multipart/form-data": {"type": "object", "properties": {
            "audio_file": {"type": "string", "format": "binary"},
        }}},
        responses={201: OpenApiTypes.OBJECT},
        description="Upload an audio file and trigger transcription.",
    )
    def post(self, request, format=None):
        audio_file = request.FILES.get("audio_file")
        if not audio_file:
            return Response({"error": "No audio_file provided"}, status=status.HTTP_400_BAD_REQUEST)

        recording = CallRecording.objects.create(audio_file=audio_file)
        run_transcription(recording.id)
        return Response({
            "message": "Upload successful. Transcription started.",
            "recording_id": recording.id
        }, status=status.HTTP_201_CREATED)
