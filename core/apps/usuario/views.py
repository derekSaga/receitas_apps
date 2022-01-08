from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request, "usuario/login.html")


def logout(request):
    return render(request, "usuario/logout.html")


def dashboard(request):
    return render(request, "usuario/dashboard.html")


def cadastro(request):
    return render(request, "usuario/cadastro.html")
