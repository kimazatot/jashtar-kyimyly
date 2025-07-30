from django.contrib import admin
from .models import ActivityDirection


@admin.register(ActivityDirection)
class ActivityDirectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)
    list_per_page = 20

    fieldsets = (
        (None, {
            'fields': ('title', 'description')
        }),
    )