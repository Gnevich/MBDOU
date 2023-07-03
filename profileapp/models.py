import datetime

from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    LastName = models.CharField("Фамилия", max_length=200, null=True, default=None)
    FirstName = models.CharField("Имя", max_length=200, null=True, default=None)
    MiddleName = models.CharField("Отчество", max_length=200, null=True, default=None)
    BornDate = models.DateField("Дата рождения", default=datetime.date.today, null=True)

    def __str__(self):
        return f"{self.LastName} {self.FirstName} {self.MiddleName}"


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


admin.site.register(Profile)
