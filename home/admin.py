from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Categoria, Evento, EventoImage, Mensagem, Usuario

admin.site.site_header = "Administração do PartyBoxd"
admin.site.site_title = "PartyBoxd"
admin.site.index_title = "Painel de administração"


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("tipo",)
    search_fields = ("tipo",)


@admin.register(Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria", "criada_em")
    list_filter = ("categoria",)
    search_fields = ("titulo", "conteudo")


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = (
        "nome",
        "categoria",
        "usuario",
        "ehPago",
        "ehPublico",
        "mediaClassificacao",
    )
    list_filter = ("categoria", "ehPago", "ehPublico")
    search_fields = ("nome", "descricao", "usuario__username", "usuario__email")


@admin.register(Usuario)
class UsuarioAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ("Campos extras", {"fields": ("data_nascimento", "bio")}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ("Campos extras", {"fields": ("data_nascimento", "bio")}),
    )
    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active")
    search_fields = ("username", "email", "first_name", "last_name")
    ordering = ("username",)


@admin.register(EventoImage)
class EventoImageAdmin(admin.ModelAdmin):
    list_display = ("evento", "image", "criado_em")
    list_filter = ("evento",)
    search_fields = ("evento__nome",)
