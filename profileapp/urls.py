from django.urls import path

from profileapp import views
from profileapp.views import profile, users, user_delete, user_detail, user_update

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', profile, name='users-profile'),
    path('users', users, name='users'),

    path('users/delete/<int:pk>', user_delete, name='user-delete'),
    path('users/update/<int:pk>', user_update, name='user-update'),
    path('users/<int:pk>', user_detail, name='user-view'),

]
