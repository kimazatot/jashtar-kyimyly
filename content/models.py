from io import BytesIO
from PIL import Image

from django.core.files.base import ContentFile
from django.core.validators import FileExtensionValidator
from django.db import models
from _common.choices.content import EventStatus


class Events(models.Model):
    title = models.CharField(max_length=99, verbose_name='Название мероприятия')
    description = models.TextField(verbose_name='Описание мероприятия')
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    date = models.DateField(verbose_name="Дата")
    event_status = models.CharField(
        max_length=255,
        verbose_name='Статус мероприятия',
        choices=EventStatus.choices
    )

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


class EventImage(models.Model):
    event = models.ForeignKey(
        Events,
        related_name='images',
        on_delete=models.CASCADE,
        verbose_name="Мероприятие"
    )
    image = models.ImageField(
        upload_to='event_photos/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
        verbose_name="Фотография"
    )

    class Meta:
        verbose_name = 'Фотография мероприятия'
        verbose_name_plural = 'Фотографии мероприятия'


class Projects(models.Model):
    title = models.CharField(max_length=155, verbose_name='Название проекта')
    description = models.TextField(verbose_name='Описание проекта')
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class ProjectsImage(models.Model):
    project = models.ForeignKey(
        Projects,
        related_name='images',
        on_delete=models.CASCADE,
        verbose_name="Проект"
    )
    image = models.ImageField(
        upload_to='project_photos/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
        verbose_name="Фотография"
    )

    class Meta:
        verbose_name = 'Фотография проекта'
        verbose_name_plural = 'Фотографии проекта'


class Gallery(models.Model):
    title = models.CharField(max_length=99, verbose_name='Название')
    date = models.DateField(verbose_name="Дата")

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'


class GalleryImage(models.Model):
    gallery = models.ForeignKey(
        Gallery,
        related_name='images',
        on_delete=models.CASCADE,
        verbose_name="Галерея"
    )
    image = models.ImageField(
        upload_to='gallery_photos/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
        verbose_name="Фотография"
    )

    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            img = img.convert('RGB')

            output = BytesIO()
            img.save(output, format='JPEG', quality=75)
            output.seek(0)

            self.image.save(self.image.name, ContentFile(output.read()), save=False)

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Фотография галереи'
        verbose_name_plural = 'Фотографии галереи'
