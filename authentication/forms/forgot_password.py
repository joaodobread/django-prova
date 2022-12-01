from django import forms
import hashlib


class ForgotPasswordForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(),
                            max_length=254, label='Email')
    reset_password_key = forms.CharField(label='Resposta de segurança', disabled=False,
                                         widget=forms.TextInput,
                                         help_text='Resposta informada durante o cadastro do usuário.', required=True)

    error_count = forms.CharField(
        widget=forms.HiddenInput,
        initial=0
    )

    new_password = forms.CharField(
        max_length=128, widget=forms.PasswordInput(), label='Nova senha')

    def clean_reset_password_key(self):
        data = self.cleaned_data
        secrey_key = data['reset_password_key'].encode()
        secret_hash = hashlib.md5(secrey_key).hexdigest()
        return secret_hash
