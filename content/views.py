from rest_framework import viewsets, generics, status
from .models import *
from drf_spectacular.utils import extend_schema
from .serializers import (EventsSerializer,
                          ProjectsSerializer,
                          ActivityDirectionSerializer,
                          DepartmentsListSerializers,
                          ResultsListSerializers,
                          NewsListSerializers)


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

class DepartmentsDetailAPIView(generics.RetrieveAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsListSerializers


class DepartmentsListAPIView(generics.RetrieveAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsListSerializers


class ResultsDetailAPIView(generics.RetrieveAPIView):
    queryset = Results.objects.all()
    serializer_class = ResultsListSerializers


class ResultsListAPIView(generics.RetrieveAPIView):
    queryset = Results.objects.all()
    serializer_class = ResultsListSerializers



class NewsDetailAPIView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializers


class NewsListAPIView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializers