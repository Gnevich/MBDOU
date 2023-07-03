from django.contrib import admin
# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from profileapp.models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    verbose_name_plural = 'Profile'


class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
