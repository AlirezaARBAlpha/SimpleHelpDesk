# gets the user_model django  default or your own custom
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from contextlib import suppress
from django.contrib.auth.hashers import check_password
from .models import *


# Class to permit the athentication using email or username
# requires to define two functions authenticate and get_user
class CustomBackend(ModelBackend):

    def authenticate(request, username=None, password=None, **kwargs):
        # Skip authentication attempts without credentials
        if username is None or password is None:
            return

        # Get user by name, check the password hash and return it if everything is ok
        with suppress(User.DoesNotExist):
            user = User.objects.get(username=username)

            if (user):
                if check_password(password, user.password):
                    return user  # Return user if credentials are correct

                else:
                    return None
            else:
                return None
        return None

    def get_user(self, slug):
        # Fetch and return user if it exists
        with suppress(User.DoesNotExist):
            return User.objects.get(slug=slug)
        return None
