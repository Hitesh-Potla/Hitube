from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from videos.models import Video
from videos.serializers import VideoSerializer

class VideoSearchView(APIView):
    def get(self, request):
        query = request.query_params.get('q', '')
        if query:
            videos = Video.objects.filter(title__icontains=query)
        else:
            videos = Video.objects.all()

        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
