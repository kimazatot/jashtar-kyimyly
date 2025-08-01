from django.db import models
from django.core.validators import FileExtensionValidator
from _common.choices.content import EventStatus



class Events(models.Model):
    title = models.CharField(max_length=99, verbose_name='Название мероприятия')
    description = models.TextField(verbose_name='Описание мероприятия')
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    date = models.DateField(verbose_name="Дата")
    event_status = models.CharField(max_length=255, verbose_name='Статус мероприятия', choices=EventStatus.choices)

    def __str__(self):
        return self.title

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
    title = models.CharField(max_length=155, verbose_name='Название проекта')
    description = models.TextField(verbose_name='Описание проекта')
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def __str__(self):
        return self.title

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

    class Meta:
        verbose_name = 'Фотография проекта'
        verbose_name_plural = 'Фотографии проекта'



class ActivityDirection(models.Model):
    title = models.CharField("Название направления", max_length=255,  blank=False,null=False)
    description = models.TextField('Описание деятельности', blank=False, null=False)


    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Направление деятельности"
        verbose_name_plural = "Направления деятельности"

    class Meta:
        verbose_name = 'Направление деятельности'
        verbose_name_plural = 'Направление деятельности'


class Departments(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название отделения')
    description = models.TextField() #RichText
    address = models.CharField(max_length=99, verbose_name='Адрес отделения')
    image = models.ImageField(
        upload_to='experts/',
        verbose_name="Изображение",
        validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'])],
        help_text="Загружайте только изображения в формате .png или .jpg или .jpeg"
    )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Региональные отделения'
        verbose_name_plural = 'Региональные отделения'


class Results(models.Model):
    title = models.TextField(verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание') #RichText

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Результаты'
        verbose_name_plural = 'Результаты'

