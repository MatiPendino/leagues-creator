from django.urls import path

from apps.liga import views

# ligas/
urlpatterns = [
    path("crear_liga", views.crear_liga, name="crear_liga")
]

