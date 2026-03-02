from django.db import models

class Event(models.Model):
    FORMAT_CHOICES = [
        ("talk", "Talk / Лекция"),
        ("workshop", "Workshop / Мастер-класс"),
        ("show", "Show / Перформанс"),
        ("expo", "Expo / Выставка"),
    ]

    title = models.CharField(max_length=220)
    description = models.TextField(blank=True)
    starts_at = models.DateTimeField()
    location = models.CharField(max_length=220, blank=True)
    speaker = models.CharField(max_length=220, blank=True)
    format = models.CharField(max_length=20, choices=FORMAT_CHOICES, default="talk")
    cover = models.ImageField(upload_to="events/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["starts_at"]

    def __str__(self):
        return f"{self.title} ({self.starts_at:%d.%m %H:%M})"