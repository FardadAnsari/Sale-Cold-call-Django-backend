import os
from django.conf import settings
import whisper
from .gemini import analyze_transcript_with_gemini
from AiAssisstanceApp.models import AgentCallTranscript, CallRecording


# Use the base Whisper model
model = whisper.load_model("base")  # or "small", "medium", etc.

def run_transcription(recording_id):
    try:
        print(f"[INFO] Starting transcription for recording ID: {recording_id}")
        recording = CallRecording.objects.get(id=recording_id)
        audio_path = os.path.join(settings.MEDIA_ROOT, str(recording.audio_file))

        # Run Whisper
        def progress(segment):
            start = round(segment['start'], 2)
            end = round(segment['end'], 2)
            text = segment['text'].strip()
            print(f"[{start:.2f} --> {end:.2f}] {text}")

        result = model.transcribe(
            recording.audio_file.path,
            verbose=False,  # We'll print manually
            task="transcribe",
            language="en",
            condition_on_previous_text=False,
            word_timestamps=False,
            temperature=0.0,
            suppress_tokens=[],
            initial_prompt=None,
            progress_callback=progress
        )
        transcript = result["text"]
        print("[INFO] Transcription complete.")
        print("Transcript:", transcript)

        # Save transcript file (optional)
        transcript_path = os.path.splitext(audio_path)[0] + ".txt"
        with open(transcript_path, "w", encoding="utf-8") as f:
            f.write(transcript)

        # Run Gemini
        gemini_response = analyze_transcript_with_gemini(transcript_path, api_key="AIzaSyBitLKpEAB16BWY5h8MI10y6AOFQfzRHiU")  # Your real API key
        print("[INFO] Gemini response received.")
        print("Gemini Output:\n", gemini_response)

        # Save to DB
        AgentCallTranscript.objects.create(
            agent_id=recording.agent_id if hasattr(recording, 'agent_id') else "unknown",
            transcript=transcript,
            summary=gemini_response,
            feedback="",  # Optional: parse from Gemini response
            score=None    # Optional: extract score
        )

    except Exception as e:
        print(f"[ERROR] Transcription or Gemini failed: {str(e)}")
