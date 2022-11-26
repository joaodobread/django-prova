from django.contrib.auth.backends import BaseBackend
from authentication.models import User


class EmailLoginBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        """
        Overrides the authenticate method to allow users to log in using their email address.
        """
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """
        Overrides the get_user method to allow users to log in using their email address.
        """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
