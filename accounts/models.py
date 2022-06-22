from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    name = models.CharField(max_length=256, default="User")
    contact = models.CharField(max_length=256, default="000-000-0000")

    def __str__(self):
        return self.username