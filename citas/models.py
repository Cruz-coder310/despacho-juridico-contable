from django.db import models
from services.models import ServicioDetalle
from phonenumber_field.modelfields import PhoneNumberField


class Cita(models.Model):
    """Model that stores client appointment information."""

    class EstadoCita(models.TextChoices):
        """Enumeration of possible appoinment statuses (estado de la cita)."""

        PENDIENTE = "PEN", "Pendiente"  # Pending
        CONTACTADO = "CON", "Contactado"  # Contacted
        CERRADA = "CER", "Cerrado"  # Closed

    name = models.CharField(max_length=100, verbose_name="Nombre Completo")
    email = models.EmailField(verbose_name="Correo Electrónico")
    phone = PhoneNumberField(
        verbose_name="Número de Teléfono",
        region="MX",
    )
    service = models.ForeignKey(
        ServicioDetalle,
        verbose_name="Servicio",
        on_delete=models.SET_NULL,
        null=True,
    )
    state = models.CharField(
        max_length=3,
        choices=EstadoCita.choices,
        verbose_name="Estado de la Consulta",
        default=EstadoCita.PENDIENTE,
    )
    description = models.TextField(
        verbose_name="Motivo de la Consulta",
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de Creación",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Última Actualización",
    )

    class Meta:
        verbose_name = "Cita"
        verbose_name_plural = "Citas"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Cita de {self.name} del {self.created_at.strftime('%d-%m-%Y')}"
