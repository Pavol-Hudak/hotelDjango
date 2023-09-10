from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CreateGuestSerializer, GuestSerializer
from .models import GuestModel
import hashlib
from django.contrib.auth.models import User

class GuestView(generics.ListAPIView):
    queryset = GuestModel.objects.all()
    serializer_class = GuestSerializer

class CreateGuestView(APIView):
    serializer_class = CreateGuestSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        print(serializer)
        if(serializer.is_valid()):
            validated_data = serializer.validated_data
            first_name = validated_data.get('first_name')
            middle_name = validated_data.get('middle_name')
            last_name = validated_data.get('last_name')
            date_of_birth = validated_data.get('date_of_birth')
            email = validated_data.get('email')
            password = validated_data.get('password')
            print(first_name,middle_name,last_name)
            print(date_of_birth,email,password)
            if GuestModel.objects.filter(email=email).exists():
                return Response({"User exists"})
            
            newGuest = GuestModel.objects.create_guest(email=email, first_name=first_name, middle_name=middle_name, last_name=last_name, date_of_birth = date_of_birth, password=password)
            return Response({"haha"})
        return Response({'Bad request':'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
    
'''class LoginGuestView(APIView):
    serializer_class = LoginGuestSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if(serializer.is_valid()):
            email = serializer.data.get('email')
            password = str(serializer.data.get('password'))
            hashedPass = hashlib.sha256(password.encode('utf-8')).hexdigest()
            queryset = Guest.objects.filter(email=email)
            if queryset.exists():
                print("user found")
                guest = queryset.first()
                print(hashedPass, guest.password) 
                if hashedPass == guest.password:
                    print("password matches")
                    return Response({'password correct'})                
                else:
                    print("user not found")
                    return Response({"User not found"})
        return Response({'Bad request':'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)'''



