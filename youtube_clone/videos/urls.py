from django.urls import path,include
from . import views 
from authentication import views as views2
from comments import views as views3
from history import urls

urlpatterns = [
    path('signup/', views2.signup_view, name='signup'),
    path('login/', views2.login_view, name='login'),
    path('logout/', views2.logout_view, name='logout'),
    path('home/', views.videos_view, name='videos'),
    # path('home/<int:video_id>/comments/', views3.comments_view, name='comments'),
    path('home/<int:video_id>', views.play_video, name='play_video'),
    path('account/upload/', views.upload_video, name='upload_video'),
    path('account/<int:video_id>/delete/', views.delete_video, name='delete_video'),
    path('account/videos/', views.get_user_videos, name='own_videos'),
    path('history/',include('history.urls'), name='history'),
]
