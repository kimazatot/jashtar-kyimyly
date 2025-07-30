from django.urls import path, include
from rest_framework import routers
from .views import ProjectList, EventList, EventsDetail, ProjectsDetail, ActivityDirectionList

router =routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),

    path('events/', EventList.as_view(), name='events-list'),
    path('events/<int:pk>/', EventsDetail.as_view(), name='events-detail'),

    path('projects/', ProjectList.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectsDetail.as_view(), name='projects-detail'),

    path('activity_direction/', ActivityDirectionList.as_view(), name='activity-direction')
]