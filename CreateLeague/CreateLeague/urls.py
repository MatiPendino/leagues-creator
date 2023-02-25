from django.contrib import admin
from django.urls import path, include
from apps.liga import urls as liga_urls
from apps.equipo import urls as equipo_urls
from apps.sitio import urls as sitio_urls
from apps.authentication import urls as auth_urls
from apps.jugador import urls as jugador_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(sitio_urls)),
    path('equipo/', include(equipo_urls)),
    path('liga/', include(liga_urls)),
    path('auth/', include(auth_urls)),
    path('jugador/', include(jugador_urls))
]
