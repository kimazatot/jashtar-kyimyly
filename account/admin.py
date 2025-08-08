from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email')