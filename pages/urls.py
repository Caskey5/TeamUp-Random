from django.urls import path

from .views import ChooseSportView, HomePageView, SportFormationView

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
    path('sports/football_formations/', SportFormationView.as_view(), name='football_formations'),

]




