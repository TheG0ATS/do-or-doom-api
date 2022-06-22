from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass
    # Include default values for both!!
    # User name? (The name the user is addressed by in texts/messages)
    # User accountability partner phone number?
    def __str__(self):
        return self.username
