from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render, redirect

from apps.equipo.models import Equipo
from apps.liga.models import Liga


def index(request):
    if request.user.username:
        ligas = Liga.objects.filter(usuario=request.user)
        equipos = Equipo.objects.filter(liga__in=ligas).select_related().order_by("-puntos", "-diferencia_goles")
    else:
        return redirect("auth/signup")

    context = {
        "ligas": ligas,
        "equipos": equipos
    }

    return render(request, "index.html", context)
