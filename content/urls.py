from django.urls import path

from .models import Gallery
from .views import ProjectList, EventList, EventsDetail, ProjectsDetail, GalleryList, GalleryDetail

urlpatterns = [
    path('events/', EventList.as_view(), name='events-list'),
    path('events/<int:pk>/', EventsDetail.as_view(), name='events-detail'),

    path('projects/', ProjectList.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectsDetail.as_view(), name='projects-detail'),

    path('images/', GalleryList.as_view(), name='images'),
    path('images/<int:pk>/', GalleryDetail.as_view(), name='images')
]