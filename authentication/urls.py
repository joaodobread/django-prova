from django.urls import path
from authentication.views import login, register, forgot_password

urlpatterns = [
    path('', login.LoginView.view, name='login_page'),
    path('register', register.RegisterView.view, name='register'),
    path('forgot_password', forgot_password.ForgotPassword.view,
         name='forgot_password'),
]
