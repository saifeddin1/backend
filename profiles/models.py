from django.db import models
from classes.models import Classe
# Create your models here.

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    cin = models.IntegerField(null=True, blank=True)
    birthdate = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    email = models.EmailField(max_length=254,  blank=True, null=True)
    classe = models.ForeignKey(
        Classe, on_delete=models.CASCADE, null=True, blank=True)
    role = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
