from django import forms
from django.contrib.auth.forms import AuthenticationForm
from authentication import models


class LoginForm(forms.Form):
    email = forms.CharField(
        max_length=500, widget=forms.EmailInput(attrs={"class": "mb-2"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "mb-2"}))

    class Meta:
        model = models.User
        fields = ('email', 'password')
