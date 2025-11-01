from django.db import models
from django.contrib.auth.models import User
from services.models import AreaServicio


class Specialist(models.Model):
    """Represents a specialist linked to a User & assigned a service type."""

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="Especialista"
    )
    area_type = models.CharField(
        max_length=2,
        choices=AreaServicio.AreaType.choices,
        verbose_name="Tipo de Servicio",
    )

    def __str__(self):
        return f"{self.user.get_full_name()} - ({self.get_area_type_display()})"

    class Meta:
        verbose_name = "Especialista"
        verbose_name_plural = "Especialistas"
        ordering = ["user__last_name"]
