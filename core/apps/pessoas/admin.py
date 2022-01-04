from core.apps.pessoas.models import Pessoa
from django.contrib import admin


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    actions = None
    search_fields = ("nome",)
    list_display = ("id", "nome", "email")
