import logging

from core.apps.usuario.serializers import UsuarioSerializer
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

logger = logging.getLogger(__name__)


# Create your views here.
def login(request):
    return render(request, "usuario/login.html")


def logout(request):
    return render(request, "usuario/logout.html")


def dashboard(request):
    return render(request, "usuario/dashboard.html")


def cadastro(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        validacao = UsuarioSerializer().validate(
            {"nome": nome, "email": email, "password": password, "password2": password2}
        )

        if validacao:
            return render(request, "usuario/cadastro.html")

        user = User.objects.create_user(
            username=nome,
            email=email,
            password=password
        )

        user.save()
        
        return redirect("usuario:login")
    else:
        return render(request, "usuario/cadastro.html")
