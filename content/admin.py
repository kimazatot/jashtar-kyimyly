from django.contrib import admin
from .models import Events, Projects, EventImage, ProjectsImage, GalleryImage, Gallery

class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 0
    max_num = 10


class ProjectImageInline(admin.TabularInline):
    model = ProjectsImage
    extra = 0
    max_num = 5

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 0
    max_num = 15


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date')
    inlines = [EventImageInline]


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    inlines = [ProjectImageInline]


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    inlines = [GalleryImageInline]