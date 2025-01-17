from django.contrib import admin
from apps.service.models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_filter = ("title",)
    list_display = ("id", "title", "sort_order")
    list_editable = ("title", "sort_order")
    search_fields = ("id",)
