from django.db import models

class CallRecording(models.Model):
    audio_file = models.FileField(upload_to='recordings/')
    agent_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Call by Agent {self.agent_id} on {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
