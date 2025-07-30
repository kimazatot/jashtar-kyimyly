from rest_framework import viewsets, generics, status
from .models import *
from drf_spectacular.utils import extend_schema
from .serializers import EventsSerializer, ProjectsSerializer, ActivityDirectionSerializer


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


class ActivityDirectionList(generics.ListAPIView):
    queryset = ActivityDirection.objects.all()
    serializer_class = ActivityDirectionSerializer