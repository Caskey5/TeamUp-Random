from django.urls import path

from .views import ChooseSportView

urlpatterns = [
    path('choose_sport/', ChooseSportView.as_view(), name='choose_sport'),
    #path('generate_team/', GeneratedTeamView.as_view(), name='generate_team'),
]