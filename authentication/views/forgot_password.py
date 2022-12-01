from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.db import transaction


from authentication.forms import forgot_password
from authentication.models import User


def find_hint_question(question_opt: str):
    questions = [
        ("1", "Cidade em que nasceu?"),
        ("2", "Qual nome do seu primeiro animal de estimação?"),
        ("3", "Seu nickname favorito em jogos?"),
        ("4", "Seu primeiro professor de programação")
    ]

    for (id, question) in questions:
        if id == question_opt:
            return question


class ForgotPassword:
    def view(request: HttpRequest):
        if request.method.lower() == 'post':
            return ForgotPassword.update_user_password(request)
        form = forgot_password.ForgotPasswordForm()
        return render(request, 'authentication/forgot_password/index.html', {"form": form})

    def update_user_password(request: HttpRequest):
        with transaction.atomic():
            form = forgot_password.ForgotPasswordForm(request.POST)
            form.full_clean()
            user = User.objects.filter(
                email=form.cleaned_data['email']).first()
            if not user:
                return render(request, 'authentication/forgot_password/index.html',
                              {"form": forgot_password.ForgotPasswordForm(), "errors": ["Usuário não encontrado"]})

            if user.reset_password_key != form.cleaned_data['reset_password_key']:
                hint = None
                error_count = int(form.cleaned_data['error_count']) + 1
                if error_count > 2:
                    hint = find_hint_question(
                        str(user.reset_password_question))
                initial = {
                    "error_count": error_count,
                    "email": form.cleaned_data['email']
                }
                return render(request, 'authentication/forgot_password/index.html', {
                    "form": forgot_password.ForgotPasswordForm(initial=initial),
                    "hint": hint,
                    "errors": ["Resposta inválida"],
                })

            user = User.objects.select_for_update().filter(
                email=form.cleaned_data['email']).first()
            user.set_password(form.cleaned_data['new_password'])
            user.save()
            return redirect('login_page')
