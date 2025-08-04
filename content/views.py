from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.generics import ListAPIView
from .models import Events, Projects, Gallery
from .serializers import EventsSerializer, ProjectsSerializer, GallerySerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['content'])
class EventList(generics.ListAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer


@extend_schema(tags=["content"])
class EventsDetail(generics.RetrieveAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer


@extend_schema(tags=['content'])
class ProjectList(generics.ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


@extend_schema(tags=["content"])
class ProjectsDetail(generics.RetrieveAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

@extend_schema(tags=['content'])
class GalleryList(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


@extend_schema(tags=['content'])
class GalleryDetail(generics.RetrieveAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
