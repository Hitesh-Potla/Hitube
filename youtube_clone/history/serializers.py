# history/serializers.py
from rest_framework import serializers
from .models import History

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['id', 'user', 'video', 'watched_at']
        read_only_fields = ['watched_at']
