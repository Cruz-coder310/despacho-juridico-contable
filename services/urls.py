from django.urls import path

from . import views

app_name = "services"
urlpatterns = [
    path("servicios/", views.areas, name="servicios"),
    path("servicio/<slug:servicio_slug>/", views.servicios, name="servicio"),
]
