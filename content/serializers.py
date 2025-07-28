from rest_framework import serializers
from .models import Events, Projects

class EventsSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def validate(self, attrs):
        if Events.objects.count() >= 10:
            raise serializers.ValidationError("Нельзя добавить больше 10 фотографий.")
        return attrs

    class Meta:
        models = Events
        fields = ('image', 'title', 'description', 'date')


class ProjectSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def validate(self, attrs):
        if Events.objects.count() >= 5:
            raise serializers.ValidationError("Нельзя добавить больше 5 фотографий.")
        return attrs

    class Meta:
        models = Projects
        fields = ('image', 'title', 'description')