from django.urls import path
from . import views

app_name = "gallery"

urlpatterns = [
    path("", views.gallery_list, name="list"),
    path("create/", views.artwork_create, name="create"),
    path("<int:pk>/", views.artwork_detail, name="detail"),

    # ❤️ лайки
    path("<int:pk>/like/", views.toggle_like, name="like"),

    # комментарии
    path("comment/<int:pk>/delete/", views.comment_delete, name="comment_delete"),
]