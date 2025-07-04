from django.shortcuts import render
from django.views import View
from AiAssisstanceApp.models import CallRecording

class UploadAudioView(View):
    def get(self, request):
        return render(request, "upload.html")

    def post(self, request):
        from django.core.files.storage import FileSystemStorage
        from .transcriber import run_transcription

        audio_file = request.FILES["audio_file"]
        fs = FileSystemStorage()
        filename = fs.save(audio_file.name, audio_file)
        uploaded_file_url = fs.url(filename)

        recording = CallRecording.objects.create(audio_file=filename)
        run_transcription(recording.id)

        return redirect("transcription-result", recording_id=recording.id)

class TranscriptionResultView(View):
    def get(self, request, recording_id):
        recording = CallRecording.objects.get(pk=recording_id)
        return render(request, "result.html", {
            "recording": recording
        })
