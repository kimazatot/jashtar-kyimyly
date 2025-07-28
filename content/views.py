from rest_framework import viewsets
from .models import ActivityDirection
from .serializers import ActivityDirectionSerializer

class ActivityDirectionViewSet(viewsets.ModelViewSet):
    queryset = ActivityDirection.objects.all()
    serializer_class = ActivityDirectionSerializer
