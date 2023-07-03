from django.contrib import admin
from schedule.models import Lesson


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1


class LessonAdmin(admin.ModelAdmin):
    list_display = ["Theme", "Group"]


admin.site.register(Lesson, LessonAdmin)
