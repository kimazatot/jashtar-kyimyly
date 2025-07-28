from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.generics import ListAPIView
from .serializers import EventsSerializer, ProjectSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['event'])
class EventList(generics.ListAPIView):
    serializer_class = EventsSerializer

@extend_schema(tags=['project'])
class EventList(generics.ListAPIView):
    serializer_class = ProjectSerializer
