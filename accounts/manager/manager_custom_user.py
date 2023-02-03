from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def _create_user(self, username, phone_number, password, **extra_fields):
        pass

    def create_user(self, username, phone_number, password, **extra_fields):
        """Create and save a regular User with the given email and password."""
        pass

    def create_superuser(self, username, phone_number, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""

        pass
