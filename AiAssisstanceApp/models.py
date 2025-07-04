from django.db import models


class CallRecording(models.Model):
    audio_file = models.FileField(upload_to='recordings/')
    agent_id = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    transcribed_text = models.TextField(blank=True, null=True)
    gemini_feedback = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Call by Agent {self.agent_id or 'Unknown'} on {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"



class AgentCallTranscript(models.Model):
    agent_id = models.CharField(max_length=100)
    transcript = models.TextField()
    summary = models.TextField()
    feedback = models.TextField()
    score = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transcript by {self.agent_id} @ {self.created_at}"
