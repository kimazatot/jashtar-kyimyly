from .views import *
from django.urls import path, include
from rest_framework import routers
from .views import ProjectList, EventList, EventsDetail, ProjectsDetail
router =routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),

    path('history/', HistoryListAPIView.as_view(), name='history_list'),
    path('history/<int:pk>/', HistoryDetailAPIView.as_view(), name='history_detail'),

    path('goals/', GoalsListAPIView.as_view(), name='goals_list'),
    path('goals/<int:pk>/', GoalsDetailAPIView.as_view(), name='goals_detail'),

    path('legislative/', LegislativeListAPIView.as_view(), name='legislative_list'),
    path('legislative/<int:pk>/', LegislativeDetailAPIView.as_view(), name='legislative_detail'),

    path('management/', ManagementListAPIView.as_view(), name='management_list'),
    path('management/<int:pk>/', ManagementDetailAPIView.as_view(), name='management_detail'),

    path('events/', EventList.as_view(), name='events-list'),
    path('events/<int:pk>/', EventsDetail.as_view(), name='events-detail'),

    path('projects/', ProjectList.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectsDetail.as_view(), name='projects-detail')
]