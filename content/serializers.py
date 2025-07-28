from rest_framework import serializers
from .models import ActivityDirection

class ActivityDirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityDirection
        fields = 'title', 'description'