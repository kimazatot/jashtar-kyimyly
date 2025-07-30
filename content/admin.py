from django.contrib import admin
from .models import *
from .models import Events, Projects, EventImage, ProjectsImage

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

class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 0
    max_num = 10


class ProjectImageInline(admin.TabularInline):
    model = ProjectsImage
    extra = 0
    max_num = 5

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date')
    inlines = [EventImageInline]

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    inlines = [ProjectImageInline]
