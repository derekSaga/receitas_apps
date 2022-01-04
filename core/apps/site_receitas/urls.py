from django.urls import path

from . import views

app_name = "site_receitas"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:receita_id>', views.receita, name='receita'),
]
