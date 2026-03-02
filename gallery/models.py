from django.db import models
from django.conf import settings


class Artwork(models.Model):
    title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=120, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="artworks/")
    tags = models.CharField(
        max_length=200,
        blank=True,
        help_text="Например: glitch, neon, ai",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    # ❤️ лайки пользователей
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="liked_artworks",
        blank=True,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()


class ArtworkComment(models.Model):
    artwork = models.ForeignKey(
        Artwork,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    text = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Comment by {self.user} on {self.artwork}"