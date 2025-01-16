from django.db import models
from django.db import models
# from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()

def validate_video_file(value):
    if not value.name.endswith(('.mp4', '.mkv', '.avi')):
        raise ValidationError('Unsupported file format.')

class Channel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

class Video(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)  # Video title
    thumbnail = models.ImageField(upload_to='thumbnails/',blank=True, null=True)  # Thumbnail image
    video_file = models.FileField(upload_to='uploads/', validators=[validate_video_file])  # Video file
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='videos')  # Reference to the user who uploaded
    upload_date = models.DateTimeField(auto_now_add=True)  # Timestamp of upload

    def __str__(self):
        return self.title
