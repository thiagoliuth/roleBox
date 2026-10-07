from django.shortcuts import render, redirect
from .forms import RoleForm
from .models import Mensagem

def index(request):
    mensagens = Mensagem.objects.all()
    return render(request, "home/index.html", {"mensagens": mensagens})


def sobre(request):
    return render(request, "home/sobre.html")

def cadastrar_role(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            # Redireciona para a página inicial (ajuste o nome da rota se necessário)
            return redirect('index')
    else:
        form = RoleForm()

    return render(request, 'home/cadastrar_role.html', {'form': form})