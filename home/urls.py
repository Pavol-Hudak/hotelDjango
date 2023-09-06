from django.urls import path
from django.shortcuts import render
from . import views
from . views import GuestView, CreateGuestView

urlpatterns = [
    path('', lambda request: render(request, 'index.html', {'key': 'value'}), name='home'),
    path('api/',GuestView.as_view()),
    path('api/register-guest', CreateGuestView.as_view())
]
