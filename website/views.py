from django.shortcuts import render

from .models import AreaServicio


def home(request):
    servicios_random = AreaServicio.objects.order_by("?")[:3]
    context = {"servicios": servicios_random}
    return render(request, "website/home.html", context)


def servicios(request):
    return render(request, "website/servicios.html", {})
