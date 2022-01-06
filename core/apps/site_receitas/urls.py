from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = "site_receitas"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:receita_id>", views.receita, name="receita"),
    path("buscar", views.buscar, name="buscar"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
