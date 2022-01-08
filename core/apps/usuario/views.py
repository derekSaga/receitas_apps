import logging

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
    if request.method == 'POST':
        logger.info('Usuario criado com sucesso')
        print('Usuario criado com sucesso')
        return redirect('usuario:login')
    else:
        return render(request, "usuario/cadastro.html")
