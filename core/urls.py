from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("accounts/signup/", views.signup, name="signup"),
]

from django.contrib import admin
from django.urls import path, include
from core.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    # остальные пути (gen, gallery, program, accounts и т.д.)
    path('gen/', include('generative.urls')),
    path('gallery/', include('gallery.urls')),
    path('program/', include('program.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # если используете встроенную аутентификацию
    path('registrations/', include('registrations.urls')),
]