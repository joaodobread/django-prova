from django.http import HttpRequest
from django.shortcuts import render, redirect
from authentication.forms import register


class RegisterView:
    def view(request: HttpRequest):
        if request.method.lower() == 'post':
            return RegisterView.register(request)
        form = register.RegisterForm()

        return render(request, 'authentication/register/index.html', {"form": form})

    def register(request: HttpRequest):

        form = register.RegisterForm(request.POST, )
        form.full_clean()
        if not form.is_valid():
            print(form.errors)
            return render(request, 'authentication/register/index.html',
                          {"form": form, "errors": form.errors})

        form.save()
        return redirect('login_page')
