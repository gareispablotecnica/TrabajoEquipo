from django.contrib import admin

from .models import Especialidad, Noticia


@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'orden', 'activa')
    list_editable = ('orden', 'activa')
    search_fields = ('nombre',)


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'publicada')
    list_filter = ('publicada', 'fecha')
    search_fields = ('titulo', 'resumen')
