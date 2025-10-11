from django.shortcuts import render

from .models import AreaServicio


def home(request):
    """Handles the request & sends random service areas to the home template."""
    servicios_random = AreaServicio.objects.order_by("?")[:3]
    context = {"servicios": servicios_random}
    return render(request, "website/home.html", context)


def areas(request):
    """Handles the request & sends categorized service areas to the services template."""
    areas_contables = AreaServicio.objects.filter(
        type=AreaServicio.AreaType.CT
    ).order_by("name")
    areas_juridicas = AreaServicio.objects.filter(
        type=AreaServicio.AreaType.JR
    ).order_by("name")
    context = {
        "areas_contables": areas_contables,
        "areas_juridicas": areas_juridicas,
    }
    return render(request, "website/servicios.html", context)
