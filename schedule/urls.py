from django.urls import path

from schedule.views import group_schedule, group_schedule_detail, lesson_detail, lesson_delete, lesson_update, \
    group_schedule_docx, survey, group_survey, survey_detail, survey_delete

urlpatterns = [
    path('group/schedule/', group_schedule, name='group-schedule'),
    path('group/schedule/<int:pk>', group_schedule_detail, name='group-schedule-detail'),
    path('lesson/<int:pk>', lesson_detail, name='lesson-detail'),
    path('lesson/<int:pk>/delete', lesson_delete, name='lesson-delete'),
    path('lesson/<int:pk>/update', lesson_update, name='lesson-update'),
    path('group/schedule/<int:pk>/docx', group_schedule_docx, name='group-schedule-docx'),

    path('group/survey/', survey, name='survey'),
    path('group/survey/<int:pk>', group_survey, name='group-survey'),
    path('survey/<int:pk>', survey_detail, name='survey-detail'),
    path('survey/<int:pk>/delete', survey_delete, name='survey-delete'),
]
