from django.contrib import admin

from .models import AreaServicio, ServicioDetalle


@admin.register(ServicioDetalle)
class ServicioDetalleAdmin(admin.ModelAdmin):
    """Display the slug field as read-only in the admin interface."""

    readonly_fields = ("slug",)


admin.site.register(AreaServicio)
