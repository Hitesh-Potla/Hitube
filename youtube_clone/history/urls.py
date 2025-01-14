from django.urls import path
from .views import *

urlpatterns = [
    path('add/', AddToHistoryView.as_view(), name='add-to-history'),
    path('list/', UserHistoryView.as_view(), name='user-history'),
    path('remove_all/', DeleteAllHistoryView.as_view(), name='remove_all'),
    path('remove_one/', DeleteOneHistoryView.as_view(), name='remove_one'),
]
