from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from videos.models import Channel

User = get_user_model()

# Generate JWT tokens
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# Signup View
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
    tokens = get_tokens_for_user(user)

    return Response({'success': True, 'message': 'User created successfully.', 'tokens': tokens}, status=status.HTTP_201_CREATED)

# Login View
@api_view(['POST'])
def login_view(request):
    data = request.data
    username = data.get('username')
    password = data.get('password')

    if not all([username, password]):
        return Response({'error': 'Both username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(request, username=username, password=password)
    if user is not None:
        tokens = get_tokens_for_user(user)
        return Response({'success': True, 'message': 'Login successful.', 'tokens': tokens}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid username or password.'}, status=status.HTTP_401_UNAUTHORIZED)

# Logout View (Handled on frontend by clearing JWT tokens)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    return Response({'success': True, 'message': 'Logout successful.'}, status=status.HTTP_200_OK)

# Create Channel
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_channel(request):
    name = request.data.get('name')
    description = request.data.get('description')

    if not name:
        return Response({'error': 'Channel name is required.'}, status=status.HTTP_400_BAD_REQUEST)

    if Channel.objects.filter(name=name).exists():
        return Response({'error': 'Channel name already exists.'}, status=status.HTTP_400_BAD_REQUEST)

    channel = Channel.objects.create(name=name, description=description, user=request.user)
    return Response({'success': True, 'message': 'Channel created successfully.'}, status=status.HTTP_201_CREATED)

# Delete Channel
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_channel(request, channel_id):
    try:
        channel = Channel.objects.get(id=channel_id)
        if channel.user != request.user:
            return Response({"error": "You are not authorized to delete this channel."}, status=status.HTTP_403_FORBIDDEN)
    except Channel.DoesNotExist:
        return Response({"error": "Channel does not exist."}, status=status.HTTP_404_NOT_FOUND)

    channel.delete()
    return Response({"message": "Channel deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
