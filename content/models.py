from django.db import models
from django.core.validators import FileExtensionValidator

class History(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'История создания'
        verbose_name_plural = 'История создания'


class Goals(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Цели и миссия'
        verbose_name_plural = 'Цели и миссия'


class Legislative(models.Model):
    law = models.CharField(max_length=155)
    file = models.FileField(
        upload_to='research/',
        blank=True,
        null=True,
        verbose_name='Файлы',
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'word', 'excel'])],
        help_text="Загружайте файлы только в формате .pdf, .word, или .excel)"
    )
    image = models.ImageField(
        upload_to='experts/',
        verbose_name="Изображение",
        validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg'])],
        help_text="Загружайте только изображения в формате .png или .jpg"
    )

    def __str__(self):
        return f'{self.law}'

    class Meta:
        verbose_name = 'Законодательная база'
        verbose_name_plural = 'Законодательная база'


class Management(models.Model):
    image = models.ImageField(
        upload_to='experts/',
        verbose_name="Изображение",
        validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg'])],
        help_text="Загружайте только изображения в формате .jpeg, .png или .jpg"
    )
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

    class Meta:
        verbose_name = 'Руководство'
        verbose_name_plural = 'Руководство'



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