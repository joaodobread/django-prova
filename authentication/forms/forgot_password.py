from django import forms
import hashlib


class ForgotPasswordForm(forms.Form):
    reset_password_key = forms.CharField(max_length=254, label='Chave Secreta')
    new_password = forms.CharField(
        max_length=128, widget=forms.PasswordInput(), label='Nova senha')

    def clean_reset_password_key(self):
        data = self.cleaned_data
        secrey_key = data['reset_password_key'].encode()
        secret_hash = hashlib.md5(secrey_key).hexdigest()
        return secret_hash
