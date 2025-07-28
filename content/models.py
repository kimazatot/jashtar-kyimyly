from django.core.validators import FileExtensionValidator
from django.db import models
from _common.choices.content import EventStatus


class Events(models.Model):
    title = models.CharField(max_length=99, verbose_name='Название мероприятия')
    description = models.TextField(verbose_name='Описание мероприятия')
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    date = models.DateField(verbose_name="Дата")
    event_status = models.CharField(max_length=255, verbose_name='Статус мероприятия', choices=EventStatus.choices)

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

class EventImage(models.Model):
    event = models.ForeignKey(Events, related_name='images', on_delete=models.CASCADE, verbose_name="Мероприятие")
    image = models.ImageField(
        upload_to='event_photos/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
        verbose_name="Фотография"
    )

    class Meta:
        verbose_name = 'Фотография мероприятия'
        verbose_name_plural = 'Фотографии мероприятия'



class Projects(models.Model):
    title = models.CharField(max_length=155, verbose_name='Название проектв')
    description = models.TextField(verbose_name='Описание проекта')
    slug = models.SlugField(max_length=255, unique=True, blank=True)


    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class ProjectsImage(models.Model):
    projects = models.ForeignKey(Projects, related_name='images', on_delete=models.CASCADE, verbose_name="Проекты")
    image = models.ImageField(
        upload_to='event_photos/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
        verbose_name="Фотография"
    )