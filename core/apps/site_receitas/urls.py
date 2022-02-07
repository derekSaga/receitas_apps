from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = "site_receitas"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:receita_id>", views.receita, name="receita"),
    path("buscar", views.buscar, name="buscar"),
    path("criar/receita", views.criar_receita, name="criar_receita"),
    path("deleta/<int:receita_id>", views.deleta_receita, name="deleta_receita"),
    path("edita/<int:receita_id>", views.edita_receita, name="edita_receita"),
    path("atualiza_receita", views.atualiza_receita, name="atualiza_receita"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
