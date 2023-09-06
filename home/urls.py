from django.urls import path
from . import views
from . views import GuestView

urlpatterns = [
    path('', views.home, name='home'),
    path('guest',GuestView.as_view())
]
