import logging
from django.shortcuts import render, redirect
from .forms import AgendaCita

logger = logging.getLogger(__name__)


def citas(request):
    """Handles the request whether it's POST or GET to show the empty form or redirect if the post is valid."""
    if request.method == "POST":
        form = AgendaCita(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            logger.info("Formulario valido. Datos recibidos: %s", data)
            return redirect("services:servicios")
        else:
            logger.warning("Formulario invalido. Errores %s:", form.errors)
    else:
        form = AgendaCita()
        logger.debug("Formulario vacion mostrado al usuario")

    return render(request, "citas/citas.html", {"form": form})

