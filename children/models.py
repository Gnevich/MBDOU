import datetime

from django.contrib.auth.models import User
from django.db import models

from profileapp.models import Profile


class GroupAge(models.Model):
    Name = models.CharField("Название", max_length=200)
    Age = models.CharField("Возраст", max_length=200)

    def __str__(self):
        return f"{self.Name} ({self.Age})"

    class Meta:
        verbose_name = "Возраст"
        verbose_name_plural = "Возраст"


class ChildrenGroup(models.Model):
    Name = models.CharField("Название группы", max_length=200)
    Mentor = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, verbose_name="Первый воспитатель", related_name='Mentor')
    SecondMentor = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, verbose_name="Второй воспитатель", related_name='SecondMentor')
    GroupAge = models.ForeignKey(GroupAge, on_delete=models.SET_NULL, null=True, verbose_name="Возраст")

    def __str__(self):
        return f"{self.GroupAge.Name} {self.Name} "

    class Meta:
        verbose_name = "Группы"
        verbose_name_plural = "Группы"


class Children(models.Model):
    LastName = models.CharField("Фамилия", max_length=200)
    FirstName = models.CharField("Имя", max_length=200)
    MiddleName = models.CharField("Отчество", max_length=200)
    BornDate = models.DateField("Дата рождения", default=datetime.date.today)
    Group = models.ForeignKey(ChildrenGroup, on_delete=models.SET_NULL, null=True, verbose_name="Группа", blank=True)
    Info = models.CharField("Информация", max_length=200, default='')
    def __str__(self):
        return f"{self.LastName} {self.FirstName} {self.MiddleName}"

    class Meta:
        verbose_name = "Дети"
        verbose_name_plural = "Дети"






