from django.contrib.auth.models import AbstractUser
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator
)
from django.db import models


class CustomUser(AbstractUser):
    reputation = models.IntegerField(
        default     = 0,
        validators  = [
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )

    def __str__(self):
        return "<CustomUser: %s>" %(self.id)
