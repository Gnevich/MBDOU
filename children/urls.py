from django.urls import path

from children.views import group, group_detail, children_update, group_update, group_delete, children_delete, \
    children_detail, children_download
from profileapp import views


urlpatterns = [
    path('group/', group, name='group'),
    path('group/<int:pk>/detail/', group_detail, name='group-detail'),

    path('children/edit/<int:pk>', children_update, name='children-update'),
    path('children/delete/<int:pk>', children_delete, name='children-delete'),
    path('children/<int:pk>', children_detail, name='children-detail'),
    path('children/<int:pk>/download', children_download, name='children-download'),

    path('group/edit/<int:pk>', group_update, name='group-update'),
    path('group/delete/<int:pk>', group_delete, name='group-delete'),

]
