from django.contrib import admin
from .models import *



@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')

@admin.register(Goals)
class  GoalsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')


@admin.register(Legislative)
class LegislativeAdmin(admin.ModelAdmin):
    list_display = ('law', 'file', 'image')


@admin.register(Management)
class ManagementAdmin(admin.ModelAdmin):
    list_display = ('image', 'first_name', 'last_name')
