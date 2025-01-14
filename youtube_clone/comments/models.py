from django.db import models
from django.db import models
# from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from videos.models import Video
User = get_user_model()

# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')  # User who commented
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='video_comments')  # Reference to the video
    comment_text = models.TextField()  # Content of the comment
    timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp of the comment
    class Meta:
        ordering = ['-timestamp']  # Latest first
    def __str__(self):
        return f"{self.user.username} - {self.video.title} - {self.comment_text[:20]}..."