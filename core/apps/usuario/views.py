import logging

from core.apps.usuario.serializers import LoginSerializer, UsuarioSerializer
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

logger = logging.getLogger(__name__)


# Create your views here.
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        validacao = LoginSerializer().validate(
            {"email": email, "password": senha}
        )
        if validacao:
            return redirect('usuario:login')
        user_name = User.objects.filter(email=email).values_list('username', flat=True).get()
        print(user_name)
        user = authenticate(request, username=user_name, password=senha)

        if user is not None:
            auth.login(request, user)    
            return redirect('usuario:dashboard')
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

        user = User.objects.create_user(username=nome, email=email, password=password)

        user.save()

        return redirect("usuario:login")
    else:
        return render(request, "usuario/cadastro.html")
