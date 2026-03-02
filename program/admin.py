from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("id", "starts_at", "title", "format", "location", "speaker")
    list_filter = ("format", "starts_at")
    search_fields = ("title", "location", "speaker", "description")
    ordering = ("starts_at",)