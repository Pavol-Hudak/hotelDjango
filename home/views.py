from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import GuestSerializer, CreateGuestSerializer
from .models import Guest

class GuestView(generics.ListAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

class CreateGuestView(APIView):
    serializer_class = CreateGuestSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if(serializer.is_valid()):
            first_name = serializer.data.get('first_name')
            middle_name = serializer.data.get('middle_name')
            last_name = serializer.data.get('last_name')
            date_of_birth = serializer.data.get('date_of_birth')
            email = serializer.data.get('email')
            queryset = Guest.objects.filter(email=email)
            if queryset.exists():
                print("User exists")
                return
            else:
                newGuest = Guest(first_name=first_name, middle_name=middle_name,
                              last_name=last_name, date_of_birth=date_of_birth, 
                              email=email)
                newGuest.save()
            return Response(GuestSerializer(newGuest).data,status=status.HTTP_201_CREATED)
        return Response({'Bad request':'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)


 