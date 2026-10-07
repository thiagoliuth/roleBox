from django.shortcuts import render, redirect
from .forms import EventoForm
from .models import Mensagem


def index(request):
    mensagens = Mensagem.objects.all()
    return render(request, "home/index.html", {"mensagens": mensagens})


def sobre(request):
    return render(request, "home/sobre.html")

def cadastrar_evento(request):
    if request.method == "POST":
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = EventoForm()

    return render(request, "home/cadastrar_role.html", {"form": form})
