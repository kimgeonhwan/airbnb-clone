from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "male"),
        (GENDER_FEMALE, "female"),
        (GENDER_OTHER, "other"),
    )

    bio = models.TextField(default="", blank=True)
    avartar = models.ImageField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True)
