from django.urls import path, include
from rest_framework import routers
from .views import ProjectList, EventList, EventsDetail, ProjectsDetail, ActivityDirectionList, DepartmentsListAPIView,DepartmentsDetailAPIView, ResultsListAPIView, ResultsDetailAPIView

router =routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),

    path('events/', EventList.as_view(), name='events-list'),
    path('events/<int:pk>/', EventsDetail.as_view(), name='events-detail'),

    path('projects/', ProjectList.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectsDetail.as_view(), name='projects-detail'),

    path('activity_direction/', ActivityDirectionList.as_view(), name='activity-direction'),

    path('departments/', DepartmentsListAPIView.as_view(), name='departments_list'),
    path('departments/<int:pk>/', DepartmentsDetailAPIView.as_view(), name='departments_detail'),

    path('results/', ResultsListAPIView.as_view(), name='results_list'),
    path('results/<int:pk>/', ResultsDetailAPIView.as_view(), name='results_detail')
]