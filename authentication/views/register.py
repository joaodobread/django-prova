from django.http import HttpRequest
from django.shortcuts import render, redirect
from authentication.forms import register
from authentication.helpers.random_words import generate_password_secret_key


class RegisterView:
    def view(request: HttpRequest):
        if request.method.lower() == 'post':
            return RegisterView.register(request)
        secret = generate_password_secret_key()
        form = register.RegisterForm(initial={
                                     "secret_key_shown": secret, "reset_password_key": secret})

        return render(request, 'authentication/register/index.html', {"form": form})

    def register(request: HttpRequest):

        form = register.RegisterForm(request.POST, )
        form.full_clean()
        if not form.is_valid():
            return render(request, 'authentication/register/index.html',
                          {"form": form, "errors": form.errors})

        form.save()
        return redirect('login_page')
