from django.contrib import admin
from .models import Estados, Pessoas

@admin.register(Estados)
class EstadosAdmin(admin.ModelAdmin):
    list_display = ('name', 'uf')  # Exibe essas colunas na lista do admin
    search_fields = ('name', 'uf')          # Permite busca pelos campos 'name' e 'uf'

@admin.register(Pessoas)
class PessoasAdmin(admin.ModelAdmin):
    list_display = ('name',)                # Exibe o campo 'name' na lista do admin
    search_fields = ('name',)               # Permite busca pelo campo 'name'
    filter_horizontal = ('estados',)        # Adiciona um widget com checkboxes para o campo 'estados'
