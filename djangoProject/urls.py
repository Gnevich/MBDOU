from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', include('profileapp.urls')),
    path('', include('schedule.urls')),
    path('', include('children.urls')),
]

admin.site.site_header = "МБДОУ 'Кораблик'"
admin.site.site_title = "МБДОУ 'Кораблик'"
admin.site.index_title = "МБДОУ 'Кораблик'"
