from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Comment
from videos.models import Video
from .serializers import CommentSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

# Video Comments View
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def comments_view(request, video_id):
    video = get_object_or_404(Video, id=video_id)

    if request.method == 'GET':
        comments = Comment.objects.filter(video=video)
        serializer = CommentSerializer(comments, many=True)
        return Response({'success': True, 'video_id': video.id, 'comments': serializer.data}, status=status.HTTP_200_OK)

    if request.method == 'POST':
        data = request.data
        comment_text = data.get('comment_text')
        if not comment_text:
            return Response({'error': 'Comment text cannot be empty.'}, status=status.HTTP_400_BAD_REQUEST)

        comment = Comment.objects.create(video=video, user=request.user, comment_text=comment_text)
        serializer = CommentSerializer(comment)
        return Response({'success': True, 'comment': serializer.data}, status=status.HTTP_201_CREATED)