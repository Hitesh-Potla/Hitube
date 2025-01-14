from rest_framework import serializers
from .models import Video, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Display username instead of user ID
    video_title = serializers.ReadOnlyField(source='video.title')  # Display video title

    class Meta:
        model = Comment
        fields = ['id', 'user', 'video', 'video_title', 'comment_text', 'timestamp']