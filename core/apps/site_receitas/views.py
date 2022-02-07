from core.apps.site_receitas.models import Receita
from django.contrib.auth.models import User
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render


def index(request):
    receitas = Receita.objects.order_by("-date_receita").filter(publicar=True).all()

    paginator = Paginator(receitas, 1)

    page = request.GET.get("page")

    receitas_por_pagina = paginator.get_page(page)
    
    dados = {"receitas": receitas_por_pagina}

    return render(request, "index.html", dados)


def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_exibir = {"receita": receita}
    return render(request, "receitas/receita.html", receita_a_exibir)


def buscar(request):

    receitas = Receita.objects.order_by("-date_receita").filter(publicar=True).all()

    if "search" in request.GET:
        termo_busca = request.GET["search"]
        if termo_busca:
            receitas = receitas.filter(nome_receita__contains=str(termo_busca).title())

    dados = {"receitas": receitas}

    return render(request, "receitas/buscar.html", dados)

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
