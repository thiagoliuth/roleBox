from django import forms
from .models import Role

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['nome', 'descricao', 'data', 'local'] 
        # Você pode estilizar os campos com widgets depois