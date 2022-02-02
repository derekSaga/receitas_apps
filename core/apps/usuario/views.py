import logging

from core.apps.site_receitas.models import Receita
from core.apps.usuario.serializers import LoginSerializer, UsuarioSerializer
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render

clogger = logging.getLogger(__name__)


# Create your views here.
def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        validacao = LoginSerializer().validate(
            {
                "email": email,
                "password": senha,
            }
        )
        if validacao:
            return redirect("usuario:login")

        user_name = (
            User.objects.filter(email=email).values_list(
                "username", flat=True).get()
        )

        user = authenticate(request, username=user_name, password=senha)

        if user is not None:
            auth.login(request, user)
            return redirect("usuario:dashboard")
    return render(request, "usuario/login.html")


def logout(request):
    auth.logout(request)
    return redirect("site_receitas:index")


def dashboard(request):
    if request.user.is_authenticated:
        receitas = Receita.objects.order_by("-date_receita").filter(
            pessoa=request.user.id
        )
        return render(request, "usuario/dashboard.html", {"receitas": receitas})
    else:
        return redirect("site_receitas:index")


def cadastro(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        validacao = UsuarioSerializer().validate(
            {"nome": nome, "email": email,
                "password": password, "password2": password2}
        )

        if validacao:
            return render(request, "usuario/cadastro.html")

        user = User.objects.create_user(
            username=nome, email=email, password=password)

        user.save()

        return redirect("usuario:login")
    else:
        return render(request, "usuario/cadastro.html")


def criar_receita(request):
    if request.method == "POST":

        user = get_object_or_404(User, pk=request.user.id)

        nome_receita = request.POST.get("nome_receita")
        ingredientes = request.POST.get("ingredientes")
        modo_preparo = request.POST.get("modo_preparo")
        tempo_preparo = request.POST.get("tempo_preparo")
        rendimento = request.POST.get("rendimento")
        categoria = request.POST.get("categoria")
        files = request.FILES.get("foto_receita")

        Receita.objects.create(
            nome_receita=nome_receita,
            ingredientes=ingredientes,
            modo_preparo=modo_preparo,
            tempo_preparo=tempo_preparo,
            rendimento=rendimento,
            categoria=categoria,
            foto_receita=files,
            pessoa=user,
        )
        return redirect("usuario:dashboard")

    return render(request, "receitas/criar_receita.html")


def deleta_receita(request, receita_id):
    with transaction.atomic():
        receita = get_object_or_404(Receita, pk=receita_id)

        receita.delete()

    return redirect("usuario:dashboard")


def edita_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_editar = {'receita': receita}

    return render(request, 'receitas/edita_receita.html', receita_a_editar)


def atualiza_receita(request):
    if request.method == 'POST':

        receita_id = request.POST.get('receita_id')
        with transaction.atomic():

            receita = get_object_or_404(Receita, pk=receita_id)

            receita.nome_receita = request.POST['nome_receita']
            receita.ingredientes = request.POST['ingredientes']
            receita.modo_preparo = request.POST['modo_preparo']
            receita.tempo_preparo = request.POST['tempo_preparo']
            receita.rendimento = request.POST['rendimento']
            receita.categoria = request.POST['categoria']

            if 'foto_receita' in request.FILES:
                receita.foto_receita = request.FILES['foto_receita']

            receita.save()
        return redirect("usuario:dashboard")
