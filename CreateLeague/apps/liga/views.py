from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.views import generic

from apps.liga.models import Liga
from apps.sitio.form import LigaForm


def crear_liga(request):
    form_liga = LigaForm()
    if request.method == "POST":
        form_liga = LigaForm(request.POST)
        if form_liga.is_valid():
            liga = form_liga.save()
            liga.usuario = request.user
            liga.save()
            liga = Liga.objects.all().last()
            return redirect("/equipo/crear_equipo/" + str(liga.id))
        else:
            form_liga = LigaForm(request.POST)
            print("Error")
            print(form_liga.errors)

    return render(request, "crear_liga.html", {'form': form_liga})
