import os
from django.core.management.base import BaseCommand
from AiAssisstanceApp.utils.transcription_utils import CallTranscriptionManager
from AiAssisstanceApp.utils.gemini_analysis import analyze_transcript_with_gemini
from AiAssisstanceApp.models import AgentCallTranscript

class Command(BaseCommand):
    help = 'Start live call transcription for a sales agent'

    def add_arguments(self, parser):
        parser.add_argument('--agent_id', type=str, required=True)

    def handle(self, *args, **options):
        agent_id = options['agent_id']
        transcriber = CallTranscriptionManager(agent_id)
        transcript_path = f"transcripts/{agent_id}.txt"

        try:
            self.stdout.write(f"🎙️ Listening for agent: {agent_id} (Press Ctrl+C to stop)")
            transcriber.run_live_transcription()

        except KeyboardInterrupt:
            self.stdout.write(self.style.WARNING("Transcription stopped. Sending to Gemini AI..."))

            try:
                # Set your Gemini API key here
                api_key = "AIzaSyBitLKpEAB16BWY5h8MI10y6AOFQfzRHiU"
                if not api_key:
                    raise ValueError("Gemini API key is missing.")

                # Call the Gemini analyzer
                response = analyze_transcript_with_gemini(transcript_path, api_key)

                with open(transcript_path, "r", encoding="utf-8") as f:
                    transcript_text = f.read()

                # Basic parsing
                summary = feedback = ""
                score = None

                if "Summary:" in response and "Feedback:" in response and "Score:" in response:
                    parts = response.split("Summary:")[1].split("Feedback:")
                    summary = parts[0].strip()
                    rest = parts[1].split("Score:")
                    feedback = rest[0].strip()
                    try:
                        score = float(rest[1].strip())
                    except ValueError:
                        score = None

                AgentCallTranscript.objects.create(
                    agent_id=agent_id,
                    transcript=transcript_text,
                    summary=summary,
                    feedback=feedback,
                    score=score,
                )

                self.stdout.write(self.style.SUCCESS("✅ Saved to database."))
                self.stdout.write(f"\nSummary: {summary}\nFeedback: {feedback}\nScore: {score}")

            except Exception as e:
                self.stderr.write(f"[ERROR] {e}")
    