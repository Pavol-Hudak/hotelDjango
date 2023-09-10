from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import GuestSerializer, CreateGuestSerializer, LoginGuestSerializer, CurrentSessionSerializer
from .models import Guest
import hashlib
from django.contrib.auth.models import User

class GuestView(generics.ListAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

class CreateGuestView(APIView):
    serializer_class = CreateGuestSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if(serializer.is_valid()):
            first_name = serializer.data.get('first_name')
            middle_name = serializer.data.get('middle_name')
            last_name = serializer.data.get('last_name')
            date_of_birth = serializer.data.get('date_of_birth')
            email = serializer.data.get('email')
            plainPassword = str(serializer.data.get('password'))
            hashedPass = hashlib.sha256(plainPassword.encode('utf-8')).hexdigest()
            current_session = self.request.session.session_key

            queryset = Guest.objects.filter(email=email)
            if queryset.exists():
                print("User exists")
                return Response({"User with this email already exists"}, status=status.HTTP_226_IM_USED)
            else:
                '''newGuest = Guest(first_name=first_name, middle_name=middle_name,
                              last_name=last_name, date_of_birth=date_of_birth, 
                              email=email, password=hashedPass,current_session=current_session)
                newGuest.save()'''

            return Response(GuestSerializer(newGuest).data,status=status.HTTP_201_CREATED)
        return Response({'Bad request':'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
    
class LoginGuestView(APIView):
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
        return Response({'Bad request':'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

class CurrentSessionView(APIView):
    serialized_class = CurrentSessionSerializer
    def get(self, request):
        serializer = self.serialized_class(data=request.data)
        if(serializer.is_valid()):
            current_session = serializer.data.get('current_session')

    
def login_guest(request):
        
        return render(request, 'index.html', {'key': 'value'})

