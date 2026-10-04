from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Categoria, Mensagem, Role, Usuario, RoleImage

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("tipo",)
    search_fields = ("tipo",)

@admin.register(Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria", "criada_em")
    list_filter = ("categoria",)
    search_fields = ("titulo", "conteudo")


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("nome", "categoria", "usuario", "ehPago", "ehPublico", "mediaClassificacao")
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

@admin.register(RoleImage)
class RoleImageAdmin(admin.ModelAdmin):
    list_display = ("role", "image", "criado_em")
    list_filter = ("role",)
    search_fields = ("role__nome",)