from django.urls import path

from apps.sitio import views

urlpatterns = [
    path("", views.index, name="index"),
]

