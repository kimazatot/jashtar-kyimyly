from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from datetime import timedelta
from django.db.models import DateTimeField
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email должен быть указан')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    fio = models.CharField('ФИО', max_length=100, validators=[RegexValidator(regex='[А-Яа-яЁё\s]{3,}',
                                                                             message='ФИО должно содержать только кириллицу и быть не короче 3 символов.')])
    email = models.EmailField(unique=True, verbose_name='email')
    is_email_verified = models.BooleanField(default=False, verbose_name=' прошёл ли пользователь верификацию email')

    is_active = models.BooleanField(verbose_name='Активен', default=False)
    date_joined = models.DateTimeField( verbose_name='Дата регистрации', auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fio']

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email

class SMSVerification(models.Model):
    email = models.EmailField(verbose_name='Email')
    code = models.CharField(max_length=4, verbose_name='Код')
    is_used = models.BooleanField(default=False, verbose_name='Использован ли код?')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return f'email Пользователя: {self.email} Код: {self.code}'

    def is_code_valid(self):
        return not self.is_used and timezone.now() < self.created_at + timedelta(minutes=3)

    class Meta:
        indexes = [
            models.Index(fields=['email', 'code']),
        ]