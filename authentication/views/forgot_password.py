from django.http import HttpRequest
from django.shortcuts import render, redirect
from authentication.forms import forgot_password
from authentication.models import User


class ForgotPassword:
    def view(request: HttpRequest):
        if request.method.lower() == 'post':
            return ForgotPassword.update_user_password(request)
        form = forgot_password.ForgotPasswordForm()
        return render(request, 'authentication/forgot_password/index.html', {"form": form})

    def update_user_password(request: HttpRequest):
        form = forgot_password.ForgotPasswordForm(request.POST)
        form.full_clean()
        user = User.objects.filter(
            reset_password_key=form.cleaned_data['reset_password_key']).first()
        if not user:
            return render(request, 'authentication/forgot_password/index.html',
                          {"form": forgot_password.ForgotPasswordForm(), "errors": ["Invalid Secret Key"]})

        user = User.objects.select_for_update().filter(
            reset_password_key=form.cleaned_data['reset_password_key']).first()
        user.set_password(form.cleaned_data['new_password'])
        user.save()
        return redirect('login_page')
