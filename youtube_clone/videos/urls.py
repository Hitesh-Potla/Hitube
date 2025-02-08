from django.urls import path, include
from . import views
from comments import views as comment_views
from subscriptions import views as subscription_views

urlpatterns = [
    # Videos
    path('videos/', views.videos_view, name='videos'),  # Home page with all videos
    path('videos/<int:video_id>/', views.play_video, name='play_video'),
    path('account/channels/<int:channel_id>/upload/', views.upload_video, name='upload_video'),
    path('account/channels/<int:channel_id>/videos/<int:video_id>/delete/', views.delete_video, name='delete_video'),
    path('account/channels/<int:channel_id>/videos/', views.get_user_videos, name='own_videos'),

    # History
    path('history/', include('history.urls'), name='history'),

    # Search
    path('search/', include('search.urls'), name='search'),

    # Subscriptions
    path('subscriptions/<int:channel_id>/subscribe/', subscription_views.subscribe, name='subscribe'),
    path('subscriptions/<int:channel_id>/unsubscribe/', subscription_views.unsubscribe, name='unsubscribe'),

    # Recommendation view
    # path('recommendations/', views.recommendations_view, name='recommendations'),

    # Like/remove like a video
    path('like/<int:video_id>/', views.like, name='like'),
    path('remove-like/<int:video_id>/', views.remove_like, name='remove_like'),

    # Include authentication URLs
    path('auth/', include('authentication.urls')),  # Delegating authentication to authentication app
]
