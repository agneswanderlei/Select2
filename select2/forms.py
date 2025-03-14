from django import forms
from .models import Pessoas
from dal import autocomplete

# class PessoasForm(forms.ModelForm):
#     class Meta:
#         model = Pessoas  # Relaciona o formulário ao modelo Pessoas
#         fields = ['name', 'estados']  # Define os campos que estarão no formulário
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome'}),
#             'estados': autocomplete.ModelSelect2Multiple(
#                 url='estados-autocomplete',
#                 attrs={'class': 'form-control'}
#             ),
#         }


class PessoasForm(forms.ModelForm):
    class Meta:
        model = Pessoas  # Relaciona o formulário ao modelo Pessoas
        fields = ['name', 'estados']  # Define os campos que estarão no formulário
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome'}),
            'estados': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }