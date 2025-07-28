from django.core.validators import FileExtensionValidator
from django.db import models
from _common.choices.content import EventStatus


class Events(models.Model):
    title = models.CharField(max_length=99, verbose_name='Название мероприятия')
    image = models.ImageField(upload_to='events/',
                              verbose_name="Изображение",
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
                              help_text="Загружайте только изображения в формате .jpg, .jpeg, или .png"
                              )
    description = models.TextField(verbose_name='Описание мероприятия')
    date = models.DateField(verbose_name="Дата")
    event_status = models.CharField(max_length=255, verbose_name='Статус мероприятия', choices=EventStatus.choices)

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


class Projects(models.Model):
    title = models.CharField(max_length=155, verbose_name='Название проектв')
    image = models.ImageField(upload_to='projects/', verbose_name="Изображение",
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
                              help_text="Загружайте только изображения в формате .jpg, .jpeg, или .png")
    description = models.TextField(verbose_name='Описание проекта')


    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'