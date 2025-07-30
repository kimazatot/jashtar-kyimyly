from .serializers import *
from rest_framework import viewsets, generics, status
from .models import *


class HistoryListAPIView(generics.ListAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializers


class HistoryDetailAPIView(generics.RetrieveAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializers


class GoalsListAPIView(generics.ListAPIView):
    queryset = Goals.objects.all()
    serializer_class = GoalsListSerializers



class GoalsDetailAPIView(generics.RetrieveAPIView):
    queryset = Goals.objects.all()
    serializer_class = GoalsListSerializers


class LegislativeListAPIView(generics.ListAPIView):
    queryset = Legislative.objects.all()
    serializer_class = LegislativeListSerializers


class LegislativeDetailAPIView(generics.RetrieveAPIView):
    queryset = Legislative.objects.all()
    serializer_class = LegislativeListSerializers


class ManagementListAPIView(generics.ListAPIView):
    queryset = Management.objects.all()
    serializer_class = ManagementListSerializers



class ManagementDetailAPIView(generics.RetrieveAPIView):
    queryset = Management.objects.all()
    serializer_class = ManagementListSerializers
=======
from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.generics import ListAPIView
from .models import Events, Projects
from .serializers import EventsSerializer, ProjectsSerializer
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
