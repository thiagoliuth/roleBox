from django import forms
from .models import Role

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['nome', 'descricao', 'data', 'local']
        # Injetamos as classes do Tailwind diretamente nos campos gerados pelo Django
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'w-full bg-[#2c3440] text-white border border-[#45556c] rounded p-2.5 mt-1 focus:outline-none focus:border-[#00e054] focus:ring-1 focus:ring-[#00e054] transition-colors'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'w-full bg-[#2c3440] text-white border border-[#45556c] rounded p-2.5 mt-1 focus:outline-none focus:border-[#00e054] focus:ring-1 focus:ring-[#00e054] transition-colors', 
                'rows': 3
            }),
            'data': forms.DateTimeInput(attrs={
                'class': 'w-full bg-[#2c3440] text-white border border-[#45556c] rounded p-2.5 mt-1 focus:outline-none focus:border-[#00e054] focus:ring-1 focus:ring-[#00e054] transition-colors',
                'type': 'datetime-local'
            }),
            'local': forms.TextInput(attrs={
                'class': 'w-full bg-[#2c3440] text-white border border-[#45556c] rounded p-2.5 mt-1 focus:outline-none focus:border-[#00e054] focus:ring-1 focus:ring-[#00e054] transition-colors'
            }),
        }