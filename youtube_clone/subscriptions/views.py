# views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Subscription
from django.contrib.auth.models import User
from videos.models import Channel

@api_view(['POST'])
def subscribe(request, channel_id):
    user = request.user
    channel = Channel.objects.get(id=channel_id)

    if Subscription.objects.filter(user=user, channel=channel).exists():
        return Response({"message": "Already subscribed"}, status=status.HTTP_400_BAD_REQUEST)

    Subscription.objects.create(user=user, channel=channel)
    return Response({"message": "Subscribed successfully"}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def unsubscribe(request, channel_id):
    user = request.user
    channel = Channel.objects.get(id=channel_id)

    subscription = Subscription.objects.filter(user=user, channel=channel)
    if not subscription.exists():
        return Response({"message": "Not subscribed"}, status=status.HTTP_400_BAD_REQUEST)

    subscription.delete()
    return Response({"message": "Unsubscribed successfully"}, status=status.HTTP_204_NO_CONTENT)
