from rest_framework import serializers
from .models import Video
from django.contrib.auth import get_user_model

User = get_user_model()

class VideoSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.StringRelatedField()  # Display the username instead of the user ID
    comments_count = serializers.SerializerMethodField()  # Custom field for comment count
    views = serializers.IntegerField()  # Include views field
    likes = serializers.IntegerField() 
    is_liked=serializers.BooleanField()
    class Meta:
        model = Video
        fields = ['id', 'title', 'thumbnail', 'video_file', 'uploaded_by', 'upload_date', 'comments_count', 'views','likes','is_liked']  # Added 'views'

    def get_comments_count(self, obj):
        return obj.comments.count()  # Return the count of comments for the video
