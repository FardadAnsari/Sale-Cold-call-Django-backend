from django.db import models

class CallRecording(models.Model):
    audio_file = models.FileField(upload_to='recordings/')
    transcribed_text = models.TextField(blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recording @ {self.created_at}"

class AgentCallTranscript(models.Model):
    agent_id = models.CharField(max_length=100)
    transcript = models.TextField()
    summary = models.TextField()
    feedback = models.TextField()
    score = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transcript by {self.agent_id} @ {self.created_at}"