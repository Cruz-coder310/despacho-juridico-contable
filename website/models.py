from django.db import models


class AreaServicio(models.Model):
    """Model representing the main service categories."""

    TIPO_SERVICIO_CHOICES = [
        ("JR", "Jurídico"),
        ("CT", "Contable"),
    ]

    name = models.CharField(
        max_length=100, unique=True, verbose_name="Nombre del Área"
    )
    description = models.TextField(
        default="Descripción pendiente",
        verbose_name="Descripción del Área de Servicio",
    )
    type = models.CharField(
        max_length=2,
        choices=TIPO_SERVICIO_CHOICES,
        verbose_name="Tipo de Servicio",
    )

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"

    class Meta:
        verbose_name = "Área de Servicio Principal"
        verbose_name_plural = "Áreas de Servicios Principales"


class ServicioDetalle(models.Model):
    """Model representing each specific service linked to an AreaServicio."""

    area = models.ForeignKey(
        AreaServicio, on_delete=models.CASCADE, verbose_name="Área de Servicio"
    )
    service_name = models.CharField(
        max_length=150, verbose_name="Nombre del Servicio Específico"
    )
    description = models.TextField(
        verbose_name="Descripción Detallada del servicio"
    )
    priority = models.IntegerField(
        default=10,
        help_text="Menor número = mayor prioridad/orden.",
        verbose_name="Prioridad/Orden",
    )

    def __str__(self):
        return f"{self.service_name} - {self.area.name}"

    class Meta:
        verbose_name = "Detalle del Servicio"
        verbose_name_plural = "Detalles de Servicios"
        ordering = ["priority"]
