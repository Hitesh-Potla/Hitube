from django.contrib import admin
from .models import Channel, Video

@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'description')
    search_fields = ('name', 'user__username')
    list_filter = ('user',)

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'channel', 'uploaded_by', 'upload_date')
    search_fields = ('title', 'channel__name', 'uploaded_by__username')
    list_filter = ('channel', 'uploaded_by', 'upload_date')
