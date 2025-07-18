import whisper
from AiAssisstanceApp.models import CallRecording
from .gemini import analyze_transcript_with_gemini
from django.db import models
import subprocess
import os
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\bin"

def load_audio_with_explicit_ffmpeg(path):
    cmd = [
        r"C:\ffmpeg\bin\ffmpeg.exe",  # full path
        "-nostdin",
        "-threads", "0",
        "-i", path,
        "-f", "f32le",
        "-ac", "1",
        "-ar", "16000",
        "-"
    ]
    out = subprocess.run(cmd, capture_output=True, check=True).stdout
    return out


# WARNING: Don't expose this key in production
GEMINI_API_KEY = "AIzaSyBitLKpEAB16BWY5h8MI10y6AOFQfzRHiU"

def run_transcription(recording_id):
    recording = CallRecording.objects.get(id=recording_id)
    model = whisper.load_model("base")

    result = model.transcribe(recording.audio_file.path, verbose=True)

    # Build line-by-line transcript with timestamps
    lines = []
    for segment in result['segments']:
        start = round(segment['start'], 2)
        end = round(segment['end'], 2)
        text = segment['text'].strip()
        lines.append(f"[{start} → {end}]: {text}")

    full_transcript = "\n".join(lines)
    recording.transcribed_text = full_transcript

    # --- GEMINI ANALYSIS ---
    try:
        print("\n===> Sending transcript to Gemini...\n")
        gemini_result = analyze_transcript_with_gemini(full_transcript, GEMINI_API_KEY)
        print("\n===> Gemini response:\n", gemini_result)
        recording.gemini_feedback = gemini_result
    except Exception as e:
        print("Gemini API failed:", str(e))
        recording.gemini_feedback = f"Gemini API failed: {str(e)}"

    recording.save()
