from django.shortcuts import render, redirect

from apps.equipo.models import Equipo
from apps.liga.models import Liga
from apps.sitio.form import EquipoForm


def crear_equipo(request, id_liga):
    liga = Liga.objects.get(id=id_liga)
    form_equipo = EquipoForm()
    if request.method == "POST":
        form_equipo = EquipoForm(request.POST)
        if form_equipo.is_valid():
            equipo = form_equipo.save()
            equipo.set_puntos(form_equipo.cleaned_data['ganados'], form_equipo.cleaned_data['empatados'])
            equipo.set_diferencia_goles(form_equipo.cleaned_data['goles_a_favor'], form_equipo.cleaned_data['goles_en_contra'])
            equipo.set_liga(liga)
            liga.cantidad_equipos += 1
            liga.save()
            equipo.save()
            return redirect("/")
        else:
            form_equipo = EquipoForm(request.POST)
            print("Error")
            print(form_equipo.errors)

    return render(request, "crear_equipo.html", {'form': form_equipo, "liga": liga})


def eliminar_equipo(request, id_equipo):
    equipo_eliminar = Equipo.objects.get(id=id_equipo)
    equipo_eliminar.delete()
    return redirect("/")


def editar_equipo(request, id_equipo):
    try:
        equipo_editar = Equipo.objects.get(id=id_equipo)
        if request.method == "GET":
            form = EquipoForm(request.POST or None, request.FILES or None, instance=equipo_editar)
        if request.method == "POST":
            form = EquipoForm(request.POST, instance=equipo_editar)
            if form.is_valid():
                equipo_editar.set_puntos(form.cleaned_data["ganados"], 
                form.cleaned_data["empatados"])
                equipo_editar.set_diferencia_goles(
                    form.cleaned_data["goles_a_favor"], form.cleaned_data["goles_en_contra"])
                equipo_editar.save()
                return redirect("/")
            else:
                print("ERROR:")
                print(form.errors)
                form = EquipoForm(request.POST, instance=equipo_editar)
    except:
        return render(request, "editar_equipo.html", {"form": form, "object": equipo_editar})
    return render(request, "editar_equipo.html", {"form": form, "object": equipo_editar})
