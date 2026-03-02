from django.urls import path
from . import views

urlpatterns = [
    path("event/<int:event_id>/", views.register_for_event, name="register_for_event"),
    path("event/<int:event_id>/unregister/", views.unregister_from_event, name="unregister_from_event"),
    path("my/", views.my_registrations, name="my_registrations"),
]