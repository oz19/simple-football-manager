from django.core.validators import (
    MaxValueValidator,
    MinValueValidator
)
from django.db import models

from users.models import CustomUser


class Challenge(models.Model):
    # Season stages
    PRE_SEASON      = 'PRE'
    FIRST_GAMES     = 'INI'
    CHRISTMAS       = 'XMS'
    CENTRAL_GAMES   = 'CEN'
    LAST_GAMES      = 'LST'
    POST_SEASON     = 'POS'

    SEASON_STAGE_CHOICES = (
        (PRE_SEASON     , 'Pre-season'),
        (FIRST_GAMES    , 'First Games'),
        (CHRISTMAS      , 'Christmas'),
        (CENTRAL_GAMES  , 'Central Games'),
        (LAST_GAMES     , 'Last Games'),
        (POST_SEASON    , 'Post-season'),
    )

    # Fields
    user                = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    target              = models.IntegerField(
        default     = 10,
        validators  = [
            MinValueValidator(1),
            MaxValueValidator(20)
        ]
    )
    current_position    = models.IntegerField(
        default     = 10,
        validators  = [
            MinValueValidator(1),
            MaxValueValidator(20)
        ]
    )
    score               = models.IntegerField(
        default     = 5,
        validators  = [
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )
    difficulty          = models.IntegerField(
        default     = 5,
        validators  = [
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )
    stage               = models.CharField(
        max_length  = 3,
        choices     = SEASON_STAGE_CHOICES,
        default     = PRE_SEASON
    )

