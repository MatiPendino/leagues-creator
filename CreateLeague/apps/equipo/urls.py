from django.urls import path

from apps.equipo import views

# equipos/
urlpatterns = [
    path('crear_equipo/<int:id_liga>', views.crear_equipo, name='crear_equipo'),
    path("eliminar_equipo/<int:id_equipo>", views.eliminar_equipo, name="eliminar_equipo"),
    path("editar_equipo/<int:id_equipo>", views.editar_equipo, name="editar_equipo")
]
