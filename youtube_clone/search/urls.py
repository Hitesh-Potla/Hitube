from django.urls import path
from .views import VideoSearchView

urlpatterns = [
    path('', VideoSearchView.as_view(), name='search'),
]
