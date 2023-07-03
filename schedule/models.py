import datetime
from django.db import models
from children.models import ChildrenGroup, Children


class CActivities(models.Model):
    Class = models.CharField("Класс", max_length=200)
    SubClass = models.CharField("Подкласс", max_length=200)

    def __str__(self):
        return f"{self.Class} ({self.SubClass})"
class Lesson(models.Model):
    Group = models.ForeignKey(ChildrenGroup, on_delete=models.SET_NULL, null=True, verbose_name="Группа", blank=True)
    Date = models.DateField("Дата", default=datetime.date.today(), null=True)
    Theme = models.CharField("Тема", max_length=200, null=True)
    Task = models.TextField("Задачи", null=True)
    Material = models.TextField("Организация предметно – пространственной развивающей среды", null=True)
    Literature = models.TextField("Используемая литература", null=True)
    Activities = models.ForeignKey(CActivities, on_delete=models.SET_NULL, null=True, verbose_name="Виды деятельности и культурные практики")
    Score = models.IntegerField("Оценка", max_length=1, null=True, default=0)

    def __str__(self):
        return f"{self.Theme}"

    class Meta:
        verbose_name = "Занятие"
        verbose_name_plural = "Занятие"
        ordering = ('Date', "Activities")


MONTH_CHOICES = (
    ("Сентябрь", "Сентябрь"),
    ("Май", "Май"),
)

ACTIVITIES_CHOICES = (
    ("Социально-комуникативное развитие", "Социально-комуникативное развитие"),
    ("Познавательное развитие", "Познавательное развитие"),
    ("Речевое развитие", "Речевое развитие"),
    ("Художественно-эстетическое развитие", "Художественно-эстетическое развитие"),
    ("Физическое развитие", "Физическое развитие"),
)

class Survey(models.Model):
    Group = models.ForeignKey(ChildrenGroup, on_delete=models.SET_NULL, null=True, verbose_name="Группа", blank=True)
    Year = models.IntegerField("Год", max_length=4, null=True)
    Season = models.CharField("Месяц", max_length=9,
                  choices=MONTH_CHOICES,
                  default="Сентябрь")
    Activities = models.CharField("Вид развития", max_length=50,
                  choices=ACTIVITIES_CHOICES,
                  default="Социально-комуникативное развитие")
    def __str__(self):
        return f"{self.Season} {self.Year}"

    class Meta:
        verbose_name = "Опросник"
        verbose_name_plural = "Опросник"
        ordering = ('Year', "Season")
class Scope(models.Model):
    Survey = models.ForeignKey(Survey, on_delete=models.SET_NULL, null=True, verbose_name="Тест", blank=True)
    Info = models.TextField("Описание", null=True)
    def __str__(self):
        return f"{self.Info}"

    class Meta:
        verbose_name = "Пункт"
        verbose_name_plural = "Пункт"
class ChildrenScopeResult(models.Model):
    Children = models.ForeignKey(Children, on_delete=models.SET_NULL, null=True, verbose_name="ФИО", blank=True)
    Result = models.IntegerField("Оценка")
    Scope = models.ForeignKey(Scope, on_delete=models.SET_NULL, null=True, verbose_name="Критерий", blank=True)
    Survey = models.ForeignKey(Survey, on_delete=models.SET_NULL, null=True, verbose_name="Тест", blank=True)
    def __str__(self):
        return f"{self.Children}"

    class Meta:
        verbose_name = "Результат"
        verbose_name_plural = "Результат"
        ordering = ('Survey', 'Children', 'Survey')



