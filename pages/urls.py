from django.urls import path

from .views import (
    BasketballFormatsView, 
    ChooseSportView, 
    FootballFormatsView, 
    HandballFormatsView, 
    HomePageView, 
    TennisFormatsView, 
    VolleyballFormatsView
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

]




