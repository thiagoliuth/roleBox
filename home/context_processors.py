from .forms import EventoForm


def evento_form(request):
    return {"evento_form": EventoForm()}
