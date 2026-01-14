from django.urls import path

from pages.views.input_view.basketball_input_view import FirstBasketballFormationInputView, SecondBasketballFormationInputView
from pages.views.input_view.football_input_view import FirstFootballFormationInputView, SecondFootballFormationInputView, ThirdFootballFormationInputView
from pages.views.input_view.handball_input_view import FirstHandballFormationInputView, SecondHandballFormationInputView
from pages.views.input_view.tennis_input_view import FirstTennisFormationInputView
from pages.views.input_view.volleyball_input_view import FirstVolleyballFormationInputView, SecondVolleyballFormationInputView, ThirdVolleyballFormationInputView

from .views import (
    HomePageView,
    ChooseSportView,
    FootballFormatsView,
    BasketballFormatsView,
    TennisFormatsView,
    HandballFormatsView,
    VolleyballFormatsView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', HomePageView.as_view(), name='about'),
    path('clients/', HomePageView.as_view(), name='clients'),
    path('contact/', HomePageView.as_view(), name='contact'),
    path('footer/', HomePageView.as_view(), name='footer'),
    path('masthead/', HomePageView.as_view(), name='masthead'),
    path('navigation/', HomePageView.as_view(), name='navigation'),
    path('portfolio_grid/', HomePageView.as_view(), name='portfolio_grid'),
    path('portfolio_models/', HomePageView.as_view(), name='portfolio_models'),
    path('services/', HomePageView.as_view(), name='services'),
    path('team/', HomePageView.as_view(), name='team'),


    path('sports/', ChooseSportView.as_view(), name='choose_sports'),


    path('sports/football_formations/', FootballFormatsView.as_view(), name='football_formats'),
    path('sports/basketball_formats/', BasketballFormatsView.as_view(), name='basketball_formats'),
    path('sports/tennis_formats/', TennisFormatsView.as_view(), name='tennis_formats'),
    path('sports/handball_formats/', HandballFormatsView.as_view(), name='handball_formats'),
    path('sports/volleyball_formats/', VolleyballFormatsView.as_view(), name='volleyball_formats'),


    path('sports/football_formations/first_formation_input/', FirstFootballFormationInputView.as_view(), name='first_football_formation_input'),
    path('sports/football_formations/second_formation_input/', SecondFootballFormationInputView.as_view(), name='second_football_formation_input'),
    path('sports/football_formations/third_formation_input/', ThirdFootballFormationInputView.as_view(), name='third_football_formation_input'),

    path('sports/basketball_formations/first_formation_input/', FirstBasketballFormationInputView.as_view(), name='first_basketball_formation_input'),
    path('sports/basketball_formations/second_formation_input/', SecondBasketballFormationInputView.as_view(), name='second_basketball_formation_input'),

    path('sports/tennis_formations/first_formation_input/', FirstTennisFormationInputView.as_view(), name='first_tennis_formation_input'),


    path('sports/handball_formations/first_formation_input/', FirstHandballFormationInputView.as_view(), name='first_handball_formation_input'),
    path('sports/handball_formations/second_formation_input/', SecondHandballFormationInputView.as_view(), name='second_handball_formation_input'),


    path('sports/volleyball_formations/first_formation_input/', FirstVolleyballFormationInputView.as_view(), name='first_volleyball_formation_input'),
    path('sports/volleyball_formations/second_formation_input/', SecondVolleyballFormationInputView.as_view(), name='second_volleyball_formation_input'),
    path('sports/volleyball_formations/third_formation_input/', ThirdVolleyballFormationInputView.as_view(), name='third_volleyball_formation_input'),

]

