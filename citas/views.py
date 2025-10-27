import logging
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .forms import CitasForm

logger = logging.getLogger(__name__)


def agendar_cita(request):
    """Handles the request whether it's POST or GET to show the empty form or redirect/reverse if the post is valid."""

    if request.method == "POST":
        form = CitasForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                logger.info("Nueva cita guardada correctamente.")
                messages.success(
                    request,
                    "¡Tu cita ha sido agendada con éxito! Te contactaremos pronto. ",
                )
                return redirect(reverse("citas:reserva"))
            except Exception as e:
                logger.error(f"Error al guardar cita: {str(e)}")
                messages.error(
                    request,
                    "Ocurrió un error inesperado. Por favor, intenta nuevamente.",
                )

        else:
            logger.warning(f"Formulario invalido. Errores: {form.errors}")
            messages.error(
                request,
                "Hubo un error en el formulario. Por favor revisa los campos marcados.",
            )
    else:
        form = CitasForm()
        logger.debug("Formulario de cita inicializado (GET request)")

    return render(request, "citas/citas.html", {"form": form})
