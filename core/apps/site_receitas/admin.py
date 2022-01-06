from core.apps.site_receitas.models import Receita
from django.contrib import admin


@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    actions = None

    list_display = ("id", "view_nome_receita", "categoria", "pessoa", "publicar")
    list_display_links = ("id", "view_nome_receita")
    search_fields = ("nome_receita",)
    readonly_fields = ("date_receita",)
    list_editable = ("publicar",)
    list_per_page = 2
    show_close_button = True

    def view_nome_receita(self, obj):
        return obj.nome_receita.title()

    view_nome_receita.short_description = "Nome Receita"
