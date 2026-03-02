from django.urls import path
from . import views

urlpatterns = [
    path('stage/', views.stage, name='stage'),
    path('api/seed/', views.seed_api, name='seed'),
]