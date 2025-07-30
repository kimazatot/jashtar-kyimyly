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
