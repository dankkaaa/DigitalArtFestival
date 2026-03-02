from django.contrib import admin
from .models import Artwork

@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author_name", "created_at")
    search_fields = ("title", "author_name", "tags")
    list_filter = ("created_at",)