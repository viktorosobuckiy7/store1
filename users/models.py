from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(null=True, blank=True, upload_to='users_images')
