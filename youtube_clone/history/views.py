from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import History
from .serializers import HistorySerializer
from videos.models import Video
from django.utils import timezone


class AddToHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        video_id = request.data.get('video_id')
        try:
            video = Video.objects.get(id=video_id)
            history, created = History.objects.get_or_create(user=request.user, video=video)
            if created:
                return Response({"message": "Video added to history."}, status=201)
            # If the video already exists in the history, update the watched_at field to move it to the top
            history.watched_at = timezone.now()  # Set the current time
            history.save()
            return Response({"message": "Video moved to the top of the history."})
        except Video.DoesNotExist:
            return Response({"error": "Video not found."}, status=404)


class UserHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        history = History.objects.filter(user=request.user)
        serializer = HistorySerializer(history, many=True)
        return Response(serializer.data)
    
    
class DeleteAllHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        # Delete all history records for the authenticated user
        History.objects.filter(user=request.user).delete()
        return Response({"message": "All history entries deleted."}, status=status.HTTP_204_NO_CONTENT)


class DeleteOneHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        video_id = request.data.get('video_id')
        if not video_id:
            return Response({"error": "Video ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Fetch the video
            video = Video.objects.get(id=video_id)
            # Fetch the history entry
            history = History.objects.get(user=request.user, video=video)
            # Delete the history entry
            history.delete()
            return Response({"message": "Video removed from history."}, status=status.HTTP_204_NO_CONTENT)

        except Video.DoesNotExist:
            return Response({"error": "Video not found."}, status=status.HTTP_404_NOT_FOUND)

        except History.DoesNotExist:
            return Response({"error": "History entry not found."}, status=status.HTTP_404_NOT_FOUND)
