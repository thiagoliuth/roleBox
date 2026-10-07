from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sobre/", views.sobre, name="sobre"),
    path("cadastrar-evento/", views.cadastrar_evento, name="cadastrar_evento"),
]
