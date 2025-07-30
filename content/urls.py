from .views import *
from django.urls import path, include
from rest_framework import routers


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

    path('departments/', DepartmentsListAPIView.as_view(), name='departments_list'),
    path('departments/<int:pk>/', DepartmentsDetailAPIView.as_view(), name='departments_detail'),

    path('results/', ResultsListAPIView.as_view(), name='results_list'),
    path('results/<int:pk>/', ResultsDetailAPIView.as_view(), name='results_detail')
]