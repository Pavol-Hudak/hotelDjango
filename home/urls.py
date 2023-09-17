from django.urls import path
from django.shortcuts import render
from . import views
from . views import GuestView, CreateGuestView, LoginGuestView, CheckAuth, Logout
urlpatterns = [
    path('', lambda request: render(request, 'index.html', {'key': 'value'}), name='home'),
    path('api/',GuestView.as_view()),
    path('api/register-guest', CreateGuestView.as_view()),
    path('api/login-guest', LoginGuestView.as_view()),
    path('api/guest-auth', CheckAuth.as_view()),
    path('api/logout',Logout.as_view()),
    path('api/get-userdata', views.get_user_data, name='get_user_data'),
    path('api/create-room',views.CreateRoomView.as_view()),
    path('api/rooms',views.RoomView.as_view()),
    path('signin', lambda request: render(request, 'index.html', {'key': 'value'}), name='signin'),
    path('profile', lambda request: render(request, 'index.html', {'key': 'value'}), name='profile')
]
