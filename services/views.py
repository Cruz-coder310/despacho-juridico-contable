from django.shortcuts import render, get_object_or_404


from .models import AreaServicio, ServicioDetalle


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
    return render(request, "services/servicios.html", context)


def servicios(request, servicio_slug):
    """handles the request & sends information about a specific service to a template"""
    servicio = get_object_or_404(ServicioDetalle, slug=servicio_slug)
    context = {"servicio": servicio}
    return render(request, "services/servicio.html", context)
