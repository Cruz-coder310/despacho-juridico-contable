from django.urls import path

from . import views

app_name = "citas"
urlpatterns = [
    path("", views.citas, name="reserva"),
]
