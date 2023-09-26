from django.forms import ModelForm
from django import forms

class SearchApplicant:

    name = forms.CharField(
        label="Buscar", max_length=50,widget=forms.TextInput(attrs={"class: input"})
    )


