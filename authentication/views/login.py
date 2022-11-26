from django.http import HttpRequest
from django.shortcuts import render
from authentication.forms import login


class LoginView:
    def get(request: HttpRequest):
        form = login.LoginForm()
        return render(request, 'login/index.html', {"form": form})

    def post(request: HttpRequest):
        return render(request, 'login/index.html')
