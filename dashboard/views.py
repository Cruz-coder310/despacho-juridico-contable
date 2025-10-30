from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
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
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_staff:
                    login(request, user)
                    return redirect("dashboard:panel")
                else:
                    messages.error(
                        request, "Acceso denegado. Solo para personal autorizado."
                    )
            else:
                messages.error(request, "Usuario o contraseña incorrectos.")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()

    context = {"form": form}

    return render(request, "dashboard/login.html", context)


def dashboard_panel(request):
    return HttpResponse("It is just a test")
