from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib import messages
from django.http import HttpResponse


def dashboard_login(request):
    """
    Handle login by authenticating members & redirect to the admin panel if
    credentials are valid, otherwise renders the login page.
    """
    if request.user.is_authenticated:
        return redirect("dashboard:panel")
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"¡Bienvenido de nuevo, {user.username}!")
            return redirect("dashboard:panel")
        # messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()

    context = {"form": form}

    return render(request, "dashboard/login.html", context)


def dashboard_panel(request):
    return HttpResponse("It is just a test")
