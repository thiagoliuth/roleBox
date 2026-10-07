from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = [
            'nome',
            'descricao',
            'dataEvento',
            'horarioEvento',
            'siglaEstado',
            'cidade',
            'bairro',
            'rua',
            'numero',
            'categoria',
            'ehPago',
            'ehPublico',
            'linkSite',
            'linkInstagram',
            'thumbnail',
            'usuario',
        ]
        # Injetamos as classes do Tailwind diretamente nos campos gerados pelo Django
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'w-full bg-[#2c3440] text-white border border-[#45556c] rounded p-2.5 mt-1 focus:outline-none focus:border-[#00e054] focus:ring-1 focus:ring-[#00e054] transition-colors'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'w-full bg-[#2c3440] text-white border border-[#45556c] rounded p-2.5 mt-1 focus:outline-none focus:border-[#00e054] focus:ring-1 focus:ring-[#00e054] transition-colors',
                'rows': 3
            }),
            'dataEvento': forms.DateInput(attrs={
                'class': 'w-full bg-[#2c3440] text-white border border-[#45556c] rounded p-2.5 mt-1 focus:outline-none focus:border-[#00e054] focus:ring-1 focus:ring-[#00e054] transition-colors',
                'type': 'date'
            }),
            'horarioEvento': forms.TimeInput(attrs={
                'class': 'w-full bg-[#2c3440] text-white border border-[#45556c] rounded p-2.5 mt-1 focus:outline-none focus:border-[#00e054] focus:ring-1 focus:ring-[#00e054] transition-colors',
                'type': 'time'
            }),
            'siglaEstado': forms.TextInput(attrs={
                'class': 'w-full bg-[#2c3440] text-white border border-[#45556c] rounded p-2.5 mt-1 focus:outline-none focus:border-[#00e054] focus:ring-1 focus:ring-[#00e054] transition-colors'
            }),
            'cidade': forms.TextInput(attrs={
                'class': 'w-full bg-[#2c3440] text-white border border-[#45556c] rounded p-2.5 mt-1 focus:outline-none focus:border-[#00e054] focus:ring-1 focus:ring-[#00e054] transition-colors'
            }),
            'bairro': forms.TextInput(attrs={
                'class': 'w-full bg-[#2c3440] text-white border border-[#45556c] rounded p-2.5 mt-1 focus:outline-none focus:border-[#00e054] focus:ring-1 focus:ring-[#00e054] transition-colors'
            }),
            'rua': forms.TextInput(attrs={
                'class': 'w-full bg-[#2c3440] text-white border border-[#45556c] rounded p-2.5 mt-1 focus:outline-none focus:border-[#00e054] focus:ring-1 focus:ring-[#00e054] transition-colors'
            }),
            'numero': forms.TextInput(attrs={
                'class': 'w-full bg-[#2c3440] text-white border border-[#45556c] rounded p-2.5 mt-1 focus:outline-none focus:border-[#00e054] focus:ring-1 focus:ring-[#00e054] transition-colors'
            }),
            'categoria': forms.Select(attrs={
                'class': 'w-full bg-[#2c3440] text-white border border-[#45556c] rounded p-2.5 mt-1 focus:outline-none focus:border-[#00e054] focus:ring-1 focus:ring-[#00e054] transition-colors'
            }),
            'ehPago': forms.CheckboxInput(attrs={
                'class': 'mt-1 h-4 w-4 rounded border-[#45556c] text-[#00e054] focus:ring-[#00e054]'
            }),
            'ehPublico': forms.CheckboxInput(attrs={
                'class': 'mt-1 h-4 w-4 rounded border-[#45556c] text-[#00e054] focus:ring-[#00e054]'
            }),
            'linkSite': forms.URLInput(attrs={
                'class': 'w-full bg-[#2c3440] text-white border border-[#45556c] rounded p-2.5 mt-1 focus:outline-none focus:border-[#00e054] focus:ring-1 focus:ring-[#00e054] transition-colors'
            }),
            'linkInstagram': forms.URLInput(attrs={
                'class': 'w-full bg-[#2c3440] text-white border border-[#45556c] rounded p-2.5 mt-1 focus:outline-none focus:border-[#00e054] focus:ring-1 focus:ring-[#00e054] transition-colors'
            }),
            'thumbnail': forms.ClearableFileInput(attrs={
                'class': 'w-full text-[#9ab] mt-1'
            }),
            'usuario': forms.Select(attrs={
                'class': 'w-full bg-[#2c3440] text-white border border-[#45556c] rounded p-2.5 mt-1 focus:outline-none focus:border-[#00e054] focus:ring-1 focus:ring-[#00e054] transition-colors'
            }),
        }