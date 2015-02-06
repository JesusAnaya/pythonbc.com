from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    photo = models.ImageField(upload_to='accounts/photos/',
                                    blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    google_plus = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)

    class Meta:
        db_table = 'auth_user'


@receiver(pre_delete, sender=User)
def user_pre_delete(sender, instance, **kwargs):
    instance.photo.delete(False)
