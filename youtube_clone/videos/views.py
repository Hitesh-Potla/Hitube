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
from .models import Video,Channel
from .serializers import VideoSerializer
from rest_framework.pagination import PageNumberPagination
from comments.models import Comment
from comments.serializers import CommentSerializer
# from .recommender import get_recommendations

# import random
# from .serializers import VideoSerializer
# from moviepy.editor import VideoFileClip
# from django.core.files.base import ContentFile
# from io import BytesIO
# from .models import Video
from django.http import Http404
from django.contrib.auth import get_user_model

User = get_user_model()

# def generate_thumbnail_from_video(video_file):
#     # Load the video clip
#     clip = VideoFileClip(video_file)

#     # Get a random time in the video (between 1% and 90% of the video's duration)
#     random_time = random.uniform(0.01, 0.9) * clip.duration
#     frame = clip.get_frame(random_time)

#     # Convert the frame to an image (PIL image)
#     from PIL import Image
#     import numpy as np

#     frame_image = Image.fromarray(np.array(frame))

#     # Save the frame as a temporary image
#     thumb_io = BytesIO()
#     frame_image.save(thumb_io, format='JPEG')
#     thumb_io.seek(0)

#     # Return the file content to be used as the thumbnail
#     return ContentFile(thumb_io.read(), name='thumbnail.jpg')

# Video List View
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def videos_view(request):
        try:
            videos = Video.objects.all()
            serializer = VideoSerializer(videos, many=True)
            return Response({'success': True, 'videos': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'success': False, 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    # try:
        # videos = get_recommendations(request.user)
        # serializer = VideoSerializer(videos, many=True)
        # return Response({'success': True, 'videos': serializer.data}, status=status.HTTP_200_OK)
    # except Exception as e:
        # Handle unexpected errors gracefully
    # return Response({'success': False, 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
#view to upload video
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_video(request,channel_id):
    if 'video_file' not in request.FILES or 'title' not in request.data:
        return Response({"error": "Both title and video file are required."}, status=status.HTTP_400_BAD_REQUEST)
    # channel=request.data.get('channel')
    video_file = request.FILES['video_file']
    title = request.data.get('title')
    user = request.user  # The currently authenticated user

    try:
        channel = Channel.objects.get(id=channel_id)
        if channel.user != user:
            return Response({"error": "You are not authorized to upload videos to this channel."}, status=status.HTTP_403_FORBIDDEN)
    except Channel.DoesNotExist:
        return Response({"error": "Channel does not exist."}, status=status.HTTP_404_NOT_FOUND)

    # Check if a thumbnail is provided
    thumbnail = request.FILES.get('thumbnail', None)
    
    # If no thumbnail is provided, generate one from the video
    # if not thumbnail:
    #     thumbnail = generate_thumbnail_from_video(video_file)

    # Create the video instance
    video = Video.objects.create(
        channel=channel,
        title=title,
        video_file=video_file,
        uploaded_by=user,
        thumbnail=thumbnail,
    )

    # Serialize and return the video data
    serializer = VideoSerializer(video)
    return Response({'success': True, 'comment': serializer.data}, status=status.HTTP_201_CREATED)

#view to delete video
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_video(request,channel_id,video_id):
    try:
        channel = Channel.objects.get(id=channel_id)
        if channel.user != request.user:
            return Response({"error": "You are not authorized to upload videos to this channel."}, status=status.HTTP_403_FORBIDDEN)
    except Channel.DoesNotExist:
        return Response({"error": "Channel does not exist."}, status=status.HTTP_404_NOT_FOUND)
    try:
        # Retrieve the video object using the video_id
        video = Video.objects.get(id=video_id,channel=channel)
        
        # Check if the authenticated user is the owner of the video
        if video.uploaded_by != request.user:
            return Response({"error": "You can only delete your own videos."}, status=status.HTTP_403_FORBIDDEN)

        # Delete the video if the user is the owner
        video.delete()
        return Response({"message": "Video deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    
    except Video.DoesNotExist:
        raise Http404  # If the video does not exist, return a 404 error

#view to list user own videos
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_videos(request,channel_id):
    videos = Video.objects.filter(channel=channel_id)
    serializer = VideoSerializer(videos, many=True)
    return Response({'success': True, 'videos': serializer.data}, status=status.HTTP_200_OK)

#view to play video
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def play_video(request, video_id):
    # Get the video by ID
    video = Video.objects.filter(id=video_id).first()

    if not video:
        return Response({'error': 'Video not found'}, status=404)

    video.views += 1
    video.save()
    
    # Get comments for the video
    comments = Comment.objects.filter(video=video)

    # Paginate comments
    paginator = PageNumberPagination()
    paginator.page_size = 10  # Set the number of comments per page
    result_page = paginator.paginate_queryset(comments, request)

    # Serialize the video and comments
    video_serializer = VideoSerializer(video)
    comment_serializer = CommentSerializer(result_page, many=True)

    return paginator.get_paginated_response({
        'success': True,
        'video': video_serializer.data,
        'comments': comment_serializer.data
    })

#view to recommend videos based on history(context based filtering)
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def video_recommendations_view(request, video_id):
#     try:
#         videos = get_recommendations(video_id)
#         serializer = VideoSerializer(videos, many=True)
#         return Response({'success': True, 'videos': serializer.data}, status=status.HTTP_200_OK)
#     except Exception as e:
#         return Response({'success': False, 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like(request, video_id):
    # Get the video by ID, return 404 if not found
    video = get_object_or_404(Video, id=video_id)

    # Check if the user has already liked the video
    if video.is_liked:
        return Response({'error': 'You have already liked this video'}, status=400)

    # Set the video as liked and increment the like count
    video.is_liked = True
    video.likes += 1  # Increment the like count
    video.save()

    return Response({'success': True, 'likes': video.likes, 'is_liked': video.is_liked})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def remove_like(request, video_id):
    # Get the video by ID, return 404 if not found
    video = get_object_or_404(Video, id=video_id)

    # Check if the user has already liked the video
    if not video.is_liked:
        return Response({'error': 'You have not liked this video yet'}, status=400)

    # Remove the like and decrement the like count
    video.is_liked = False
    video.likes -= 1  # Decrement the like count
    video.save()

    return Response({'success': True, 'likes': video.likes, 'is_liked': video.is_liked})