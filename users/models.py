from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    reputation = models.IntegerField(default=0)

    def __str__(self):
        return "<CustomUser: %s>" %(self.id)
