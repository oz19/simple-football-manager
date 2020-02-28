from django.core.validators import (
    MaxValueValidator,
    MinValueValidator
)
from django.db import models

from users.models import CustomUser


class Budget(models.Model):
    season_budget       = models.IntegerField(
        default     = 0,
        validators  = [
            MinValueValidator(0),
            MaxValueValidator(1000000000)
        ]
    )
    cash                = models.IntegerField(
        default     = 0,
        validators  = [
            MinValueValidator(0),
            MaxValueValidator(1000000000)
        ]
    )
    players             = models.IntegerField(
        default     = 0,
        validators  = [
            MinValueValidator(0),
            MaxValueValidator(1000000000)
        ]
    )
    staff               = models.IntegerField(
        default     = 0,
        validators  = [
            MinValueValidator(0),
            MaxValueValidator(1000000000)
        ]
    )
    bonus               = models.IntegerField(
        default     = 0,
        validators  = [
            MinValueValidator(0),
            MaxValueValidator(1000000000)
        ]
    )
    marketing           = models.IntegerField(
        default     = 0,
        validators  = [
            MinValueValidator(0),
            MaxValueValidator(1000000000)
        ]
    )
    team_building       = models.IntegerField(
        default     = 0,
        validators  = [
            MinValueValidator(0),
            MaxValueValidator(1000000000)
        ]
    )
    education           = models.IntegerField(
        default     = 0,
        validators  = [
            MinValueValidator(0),
            MaxValueValidator(1000000000)
        ]
    )
    facilities          = models.IntegerField(
        default     = 0,
        validators  = [
            MinValueValidator(0),
            MaxValueValidator(1000000000)
        ]
    )


class Challenge(models.Model):
    # Season stages
    PRE_SEASON      = 0
    FIRST_GAMES     = 1
    CHRISTMAS       = 2
    CENTRAL_GAMES   = 3
    LAST_GAMES      = 4
    POST_SEASON     = 5

    SEASON_STAGE_CHOICES = (
        (PRE_SEASON     , 'Pre-season'),
        (FIRST_GAMES    , 'First Games'),
        (CHRISTMAS      , 'Christmas'),
        (CENTRAL_GAMES  , 'Central Games'),
        (LAST_GAMES     , 'Last Games'),
        (POST_SEASON    , 'Post-season'),
    )

    # Fields
    user                = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    budget              = models.OneToOneField(Budget, on_delete=models.CASCADE, null=True)
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
    stage               = models.IntegerField(
        choices     = SEASON_STAGE_CHOICES,
        default     = PRE_SEASON,
        validators  = [
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
    )

