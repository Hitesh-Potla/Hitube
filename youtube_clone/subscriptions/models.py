# models.py
from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from videos.models import Channel
User = get_user_model()

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'channel']
