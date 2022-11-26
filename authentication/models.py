from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    email = models.EmailField(unique=True, error_messages={
                              'unique': 'Email já existe.'})
    username = models.CharField(max_length=150, null=True)
    reset_password_key = models.CharField(
        'user_reset_password_key', 'reset_password_key', max_length=254)
