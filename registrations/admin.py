from django.contrib import admin
from .models import Registration

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "user", "event")
    list_filter = ("created_at",)
    search_fields = ("user__username", "user__email", "event__title")