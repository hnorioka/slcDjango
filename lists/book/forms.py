from django import forms
from .models import Item


class ItensForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['nome', 'quantidade']