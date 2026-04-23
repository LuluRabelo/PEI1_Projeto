#Define o formulário
from  django import forms
from .models import Curriculo
#Cria um formulário baseado no model
class CurriculoForm(forms.ModelForm):
    class Meta:
    #Diz para usar todos os campos do model Curriculo no formulário
        model = Curriculo
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu nome completo'
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(00) 00000-0000'
            }),
            'formacao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Ex: Ensino Médio, Curso Técnico...'
            }),
            'experiencia': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descreva suas experiências'
            }),
        }

        labels = {
    'nome': 'Nome completo',
    'telefone': 'Telefone',
    'formacao': 'Formação acadêmica',
}