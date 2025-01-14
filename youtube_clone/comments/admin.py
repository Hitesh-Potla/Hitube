from django.contrib import admin
from .models import Comment

# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'video', 'timestamp')
    search_fields = ('user__username', 'video__title', 'comment_text')
    list_filter = ('timestamp',)