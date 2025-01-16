from django.shortcuts import render
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
from django.contrib.auth import get_user_model
from videos.models import *

User = get_user_model()

# Signup View
@csrf_exempt
@api_view(['POST'])
def signup_view(request):
    data = request.data
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirm_password')

    if not all([username, email, password, confirm_password]):
        return Response({'error': 'All fields are required.'}, status=status.HTTP_400_BAD_REQUEST)

    if password != confirm_password:
        return Response({'error': 'Passwords do not match.'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, email=email, password=password)
    return Response({'success': True, 'message': 'User created successfully.'}, status=status.HTTP_201_CREATED)

# Login View
@csrf_exempt
@api_view(['POST'])
def login_view(request):
    data = request.data
    username = data.get('username')
    password = data.get('password')

    if not all([username, password]):
        return Response({'error': 'Both username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({'success': True, 'message': 'Login successful.'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid username or password.'}, status=status.HTTP_401_UNAUTHORIZED)

# Logout View
@csrf_exempt
@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({'success': True, 'message': 'Logged out successfully.'}, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['POST'])
def create_channel(request):
    name = request.data.get('username')
    description = request.data.get('password')
    if not name:
        return Response({'error': 'Channel name is required.'}, status=status.HTTP_400_BAD_REQUEST)
    if Channel.objects.filter(name=name).exists():
        return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)
    channel = Channel.objects.create(name=name, description=description)
    return Response({'success': True, 'message': 'Channel created successfully.'}, status=status.HTTP_201_CREATED)
@csrf_exempt
@api_view(['POST'])
def delete_channel(request,channel_id):
    try:
        channel = Channel.objects.get(id=channel_id)
        if channel.user!=request.user:
            return Response({"error": "You are not authorized to delete this channel."}, status=status.HTTP_403_FORBIDDEN)
    except Channel.DoesNotExist:
        return Response({"error": "Channel does not exist."}, status=status.HTTP_404_NOT_FOUND)
    channel.delete()
    return Response({"message": "Channel Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)