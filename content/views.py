from rest_framework import generics
from .models import ActivityDirection
from .serializers import ActivityDirectionSerializer

class ActivityDirection(generics.ListAPIView):
    queryset = ActivityDirection.objects.all()
    serializer_class = ActivityDirectionSerializer
