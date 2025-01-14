from django.db import models
from django.conf import settings
from videos.models import Video  # Assuming you have a Video model in the videos app
from django.contrib.auth import get_user_model
User = get_user_model()

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    watched_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-watched_at']  # Latest first

    def __str__(self):
        return f"{self.user.username} watched {self.video.title}"
