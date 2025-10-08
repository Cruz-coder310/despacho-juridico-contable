from django.shortcuts import render

from .models import AreaServicio


def home(request):
    servicios = AreaServicio.objects.all()
    context = {"servicios": servicios}
    return render(request, "website/home.html", context)
