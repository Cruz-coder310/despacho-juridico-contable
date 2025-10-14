from django.urls import path

from . import views

app_name = "services"
urlpatterns = [
    path("servicios/", views.areas, name="servicios"),
    path("servicio/<slug:servicio_slog>/", views.servicios, name="servicio"),
]
