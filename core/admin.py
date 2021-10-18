from django.contrib import admin
from core.models import Evento

# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao') #mostra quais colunas são exibidas
    list_filter = ('titulo', ) #cria um campo de filtro -- IMPORTANTE DEIXAR VÍRGULA NO FINAL
admin.site.register(Evento, EventoAdmin)