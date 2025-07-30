from django.urls import path
from .views import ActivityDirectionListAPIView  # Исправлено на правильное имя класса

urlpatterns = [
    path('directions/', ActivityDirectionListAPIView.as_view(), name='activity-direction-list'),
]