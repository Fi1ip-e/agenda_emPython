from django import forms
from .models import TbAgenda

class Contato(forms.Form):
    nome = forms.CharField(label = 'Nome', max_length=100)
    email = forms.CharField(label = 'Email', max_length=100)
    contato = forms.CharField(label = 'Contato', max_length=100)


class AddContato(forms.ModelForm):
    class Meta:
        model = TbAgenda
        fields = ['nome', 'email', 'contato']