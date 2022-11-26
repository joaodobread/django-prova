from django import forms
from authentication.helpers.random_words import generate_password_secret_key
from authentication.models import User
import hashlib
from django.contrib.auth.hashers import make_password


class RegisterForm(forms.ModelForm):
    generated_key = generate_password_secret_key()
    email = forms.CharField(widget=forms.EmailInput(),
                            max_length=254, label='Email')
    password = forms.CharField(
        widget=forms.PasswordInput(), max_length=128, label='Senha')
    first_name = forms.CharField(max_length=150, label='Nome')
    last_name = forms.CharField(max_length=150, label='Sobrenome', )
    secret_key_shown = forms.CharField(initial=generated_key, label='Chave de Recuperação de senha', disabled=True,
                                       help_text='Salve em um lugar seguro, pois esse campo só é exibido agora. Depois do cadastro nunca mais será exibido.', )
    reset_password_key = forms.CharField(
        initial=generated_key, widget=forms.HiddenInput)

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name',
                  'last_name', 'reset_password_key')

    def clean_reset_password_key(self):
        data = self.cleaned_data
        secrey_key = data['reset_password_key'].encode()
        secret_hash = hashlib.md5(secrey_key).hexdigest()
        return secret_hash

    def clean_password(self):
        data = self.cleaned_data
        hashed_password = make_password(data['password'])
        return hashed_password