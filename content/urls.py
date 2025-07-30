from django.urls import path
from .views import ActivityDirection  # Исправлено на правильное имя класса

urlpatterns = [
    path('', ActivityDirection.as_view(), name='activity-direction-list'),
]