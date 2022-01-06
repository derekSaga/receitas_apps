from core.apps.site_receitas.models import Receita
from django.shortcuts import get_object_or_404, render


def index(request):
    receitas = Receita.objects.order_by('-date_receita').filter(publicar=True).all()

    dados = {"receitas": receitas}

    return render(request, "../templates/index.html", dados)


def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_exibir = {
        'receita': receita
    }
    return render(
        request, "../templates/receita.html", receita_a_exibir
    )
