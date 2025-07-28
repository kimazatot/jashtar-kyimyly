from django.db import models

class ActivityDirection(models.Model):
    title = models.CharField("Название направления", max_length=255,  blank=False,null=False)
    description = models.TextField('Описание деятельности', blank=False, null=False)

    def __str__(self):
        return self.title
