from django.contrib import admin

from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "duration_minutes")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "description")
    exclude = ("is_featured",)
