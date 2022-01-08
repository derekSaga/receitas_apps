from core.apps.site_receitas.models import Receita
from django.shortcuts import get_object_or_404, render


def index(request):
    receitas = Receita.objects.order_by("-date_receita").filter(publicar=True).all()

    dados = {"receitas": receitas}

    return render(request, "index.html", dados)


def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_exibir = {"receita": receita}
    return render(request, "receita.html", receita_a_exibir)


def buscar(request):

    receitas = Receita.objects.order_by("-date_receita").filter(publicar=True).all()

    if "search" in request.GET:
        termo_busca = request.GET["search"]
        if termo_busca:
            receitas = receitas.filter(nome_receita__contains=termo_busca)

    dados = {"receitas": receitas}

    return render(request, "buscar.html", dados)
