from django.contrib import admin

from .models import Children, ChildrenGroup


class ChildrenInline(admin.TabularInline):
    model = Children
    extra = 1


class ChildrenAdmin(admin.ModelAdmin):
    list_display = ["LastName", "FirstName", "MiddleName"]


class ChildrenGroupAdmin(admin.ModelAdmin):
    inlines = [ChildrenInline]
    list_display = ["Name", "Mentor"]


admin.site.register(Children, ChildrenAdmin)
admin.site.register(ChildrenGroup, ChildrenGroupAdmin)




