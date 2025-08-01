from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from .models import Events, Projects, EventImage, ProjectsImage, ActivityDirection, Departments, Results


class ActivityDirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityDirection
        fields = 'title', 'description'

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectsImage
        fields = ('id', 'image')


class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImage
        fields = ('id', 'image')


class ProjectsSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializer(many=True, required=False)

    class Meta:
        model = Projects
        fields = ('id', 'title', 'description', 'images')

    def create(self, validated_data):
        images_data = self.initial_data.getlist('images')
        if len(images_data) > 5:
            raise serializers.ValidationError("Можно загрузить максимум 5 изображений.")

        project = Projects.objects.create(
            title=validated_data['title'],
            description=validated_data['description']
        )

        for image in images_data:
            ProjectsImage.objects.create(project=project, image=image)
        return project


class EventsSerializer(serializers.ModelSerializer):
    images = EventImageSerializer(many=True, required=False)

    class Meta:
        model = Events
        fields = ('id', 'title', 'description', 'date', 'images')

    def create(self, validated_data):
        images_data = self.initial_data.getlist('images')
        if len(images_data) > 10:
            raise serializers.ValidationError("Можно загрузить максимум 10 изображений.")

        event = Events.objects.create(
            title=validated_data['title'],
            description=validated_data['description'],
            date=validated_data['date']
        )

        for image in images_data:
            EventImage.objects.create(event=event, image=image)
        return event

class DepartmentsListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ['title', 'description', 'address', 'image']


class ResultsListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = ['title', 'description']