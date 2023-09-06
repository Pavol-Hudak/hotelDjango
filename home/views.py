from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import GuestSerializer
from .models import Guest

class GuestView(generics.ListAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


def home(request):
    return render(request,'index.html')
 