from django.urls import path

from surveys import views

app_name = 'surveys'

urlpatterns = [
    path('', views.survey_list, name='survey_list'),
    path('survey/<int:survey_id>/', views.survey_process, name='survey_process'),
    path('survey/finished/', views.survey_finished, name='survey_finished'),
]
