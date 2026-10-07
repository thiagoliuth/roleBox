from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sobre/", views.sobre, name="sobre"),
    path("cadastrar-role/", views.cadastrar_role, name="cadastrar_role"),
]
