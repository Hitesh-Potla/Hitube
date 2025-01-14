from django.contrib import admin
from .models import Video

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_by', 'upload_date')
    search_fields = ('title', 'uploaded_by__username')
    list_filter = ('upload_date',)


