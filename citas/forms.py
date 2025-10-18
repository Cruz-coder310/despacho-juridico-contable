from django import forms
from services.models import ServicioDetalle

from django.utils import timezone
from django.core.exceptions import ValidationError


class AgendaCita(forms.Form):
    """Form that Handles the Cita for a Service"""

    name = forms.CharField(label="Nombre Completo", max_length=100)
    email = forms.EmailField(label="Correo Elctronico(email)")
    phone = forms.CharField(label="Numero de Telefono", max_length=15)
    service = forms.ModelChoiceField(
        queryset=ServicioDetalle.objects.all(), label="Servicio"
    )
    date = forms.DateField(
        label="Fecha Deseada para la Cita",
        widget=forms.DateInput(attrs={"type": "date"}),
    )
    time = forms.TimeField(
        label="Hora Deseada para la Cita",
        widget=forms.TimeInput(attrs={"type": "time"}),
    )

    description = forms.CharField(
        label="Motivo de Cita", widget=forms.Textarea, required=False
    )

    MODALIDAD_CHOICES = [
        ("presencial", "Presencial"),
        ("videollamada", "Videollamada"),
        ("telefono", "Telefono"),
    ]
    modalidad = forms.ChoiceField(choices=MODALIDAD_CHOICES, label="Modalidad")

    def clean_phone(self):
        """Valid if phone has just numbers."""
        phone_number = self.cleaned_data.get("phone")
        if phone_number and not phone_number.isdigit():
            raise ValidationError("Por favor, ingresa solo numeros en el teléfono.")

    def clean_date(self):
        """Valid if the date is not in the past"""
        cita_date = self.cleaned_data.get("date")

        if cita_date and cita_date < timezone.localdate():
            raise ValidationError("No puedes agendar una cita en una fecha pasada")
