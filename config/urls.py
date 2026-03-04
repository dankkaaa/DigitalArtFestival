from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("gen/", include("generative.urls")),
    path("gallery/", include(("gallery.urls", "gallery"), namespace="gallery")),
    path("program/", include("program.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("registrations/", include("registrations.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)