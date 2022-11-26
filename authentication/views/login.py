from django.http import HttpRequest
from django.shortcuts import render, redirect
from authentication.forms import login as login_forms
from django.contrib.auth import authenticate, login


class LoginView:
    def view(request: HttpRequest):
        if request.method.lower() == 'post':
            return LoginView.post(request)

        form = login_forms.LoginForm()
        return render(request, 'authentication/login/index.html', {"form": form})

    def post(request: HttpRequest):
        form = login_forms.LoginForm(request.POST)
        form.full_clean()
        if not form.is_valid():
            return render(request, 'authentication/login/index.html', {"form": form, "errors": ["Dados inválidos"]})
        user = authenticate(request, email=form.cleaned_data.get('email'),
                            password=form.cleaned_data.get('password'))
        login(request, user)
        if not user:
            return render(request, 'authentication/login/index.html', {"form": form, "errors": ["Usuário não encontrado ou credenciais invalidas"]})
        return redirect('dashboard')
