from django.urls import path

from account.views import (
    AccountLoginView,
    AccountLogoutView,
    HistoryView,
    SaveGenerationView,
    SavedGenerationDetailView,
    SignUpView,
)

app_name = 'account'

urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', AccountLogoutView.as_view(), name='logout'),
    path('history/', HistoryView.as_view(), name='history'),
    path('history/<int:pk>/', SavedGenerationDetailView.as_view(), name='saved_generation'),
    path('save/<int:pk>/', SaveGenerationView.as_view(), name='save_generation'),
]
