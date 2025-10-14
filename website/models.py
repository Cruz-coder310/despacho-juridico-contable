# from django.db import models
# from django.utils.text import slugify
# from django.core.validators import MinValueValidator, MaxValueValidator
#
#
# class AreaServicio(models.Model):
#     """Represents a primary service category."""
#
#     class AreaType(models.TextChoices):
#         """Enumeration of available service area types."""
#
#         JR = "JR", "Jurídico"
#         CT = "CT", "Contable"
#
#     name = models.CharField(max_length=100, unique=True, verbose_name="Nombre del Área")
#     description = models.TextField(
#         default="Descripción pendiente",
#         verbose_name="Descripción del Área de Servicio",
#     )
#     type = models.CharField(
#         max_length=2,
#         choices=AreaType.choices,
#         verbose_name="Tipo de Servicio",
#     )
#
#     def __str__(self):
#         return f"{self.name} ({self.get_type_display()})"
#
#     class Meta:
#         verbose_name = "Área de Servicio Principal"
#         verbose_name_plural = "Áreas de Servicios Principales"
#
#
# class ServicioDetalle(models.Model):
#     """Represent a speecific service linked to an AreaServicio."""
#
#     area = models.ForeignKey(
#         AreaServicio, on_delete=models.CASCADE, verbose_name="Área de Servicio"
#     )
#     name = models.CharField(
#         max_length=150, verbose_name="Nombre del Servicio Específico"
#     )
#     description = models.TextField(verbose_name="Descripción Detallada del servicio")
#     priority = models.PositiveSmallIntegerField(
#         default=10,
#         validators=[MinValueValidator(1), MaxValueValidator(10)],
#         help_text="Menor número = mayor prioridad/orden.",
#         verbose_name="Prioridad/Orden",
#     )
#     slug = models.SlugField(max_length=120, unique=True, blank=True)
#
#     def save(self, *args, **kwargs):
#         """Updates the slug if the name has changed or if the instance is new."""
#         if not self.pk or ServicioDetalle.objects.get(pk=self.pk).name != self.name:
#             self.slug = slugify(self.name)
#         super().save(*args, **kwargs)
#
#     def __str__(self):
#         return f"{self.name} - {self.area.name}"
#
#     class Meta:
#         verbose_name = "Detalle del Servicio"
#         verbose_name_plural = "Detalles de Servicios"
#         ordering = ["priority"]
