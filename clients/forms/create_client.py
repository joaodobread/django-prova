from django import forms
from clients.models import Client


class CreateClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
