from django.urls import path

from .views import IndexPageView

paterns = [
    path('', IndexPageView.as_view(), name='index'),
]