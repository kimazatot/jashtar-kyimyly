from .models import *
from rest_framework import serializers


class HistorySerializers(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['title', 'description', 'image']


class GoalsListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Goals
        fields = ['title', 'description', 'image']


class LegislativeListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Legislative
        fields = ['law', 'file', 'image']


class ManagementListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Management
        fields = ['first_name', 'last_name']

