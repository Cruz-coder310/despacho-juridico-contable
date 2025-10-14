from django.shortcuts import render

from services.models import AreaServicio


def home(request):
    """Handles the request & sends random service areas to the home tamplate."""
    servicios_random = AreaServicio.objects.order_by("?")[:3]
    context = {"servicios": servicios_random}
    return render(request, "core/home.html", context)
