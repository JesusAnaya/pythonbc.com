from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    photo = models.ImageField(upload_to='accounts/photos/',
                                    blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    google_plus = models.URLField(blank=True, null=True)

    class Meta:
        db_table = 'auth_user'

