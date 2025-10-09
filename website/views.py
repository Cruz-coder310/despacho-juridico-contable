from django.shortcuts import render

from .models import AreaServicio


def home(request):
    servicios_random = AreaServicio.objects.order_by("?")[:3]
    context = {"servicios": servicios_random}
    return render(request, "website/home.html", context)


def servicios(request):
    servicios_contables = AreaServicio.objects.filter(type="CT").order_by("name")
    servicios_juridicos = AreaServicio.objects.filter(type="JR").order_by("name")
    context = {
        "servicios_contables": servicios_contables,
        "servicios_juridicos": servicios_juridicos,
    }
    return render(request, "website/servicios.html", context)
