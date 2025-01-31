from django.db import models
# from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()

def validate_video_file(value):
    if not value.name.endswith(('.mp4', '.mkv', '.avi')):
        raise ValidationError('Unsupported file format.')

class Tag(models.Model):
    name = models.CharField(max_length=50)

class Channel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

class Video(models.Model):
    # Existing fields
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    # tags = models.ManyToManyField(Tag)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    video_file = models.FileField(upload_to='uploads/', validators=[validate_video_file])
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='videos')
    upload_date = models.DateTimeField(auto_now_add=True)
    
    # New fields
    views = models.PositiveIntegerField(default=0)  # Number of views
    likes = models.PositiveIntegerField(default=0)  # Number of likes
    is_liked=models.BooleanField(default=False)
    category = models.CharField(max_length=50, blank=True, null=True)  # Video category

    def __str__(self):
        return self.title
