from django.db import models

# Create your models here.

class AgentCallTranscript(models.Model):
    agent_id = models.CharField(max_length=100)
    transcript = models.TextField()
    summary = models.TextField(blank=True)
    feedback = models.TextField(blank=True)
    score = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Call by {self.agent_id} on {self.created_at.strftime('%Y-%m-%d %H:%M')}"