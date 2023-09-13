from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView, View
from .serializers import CreateGuestSerializer, GuestSerializer, LoginGuestSerializer, LoginSerializer
from .models import GuestModel
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import get_token
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class GuestView(generics.ListAPIView):
    queryset = GuestModel.objects.all()
    serializer_class = GuestSerializer

class CreateGuestView(APIView):
    serializer_class = CreateGuestSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        print(serializer, "bb")
        if not serializer.is_valid():
            print(serializer.errors, "aa")
            return Response({'Serializer error'}, status=status.HTTP_400_BAD_REQUEST)
        
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
            return Response({"User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        newGuest = GuestModel.objects.create_guest(email=email, first_name=first_name, middle_name=middle_name, last_name=last_name, 
                                                    date_of_birth = date_of_birth, password=password)
        if newGuest is None:
            return Response({"User was not created"}, status=status.HTTP_417_EXPECTATION_FAILED)
        return Response({"User successfully"}, status=status.HTTP_201_CREATED)
    
class LoginGuestView(APIView):
    serializer_class = LoginSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'Serializer error'}, status=status.HTTP_400_BAD_REQUEST)
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            print("User logged in")
            login(request,user)
            return Response({"good"})
        else:
            print("User not logged in")
            return Response({"bad"})

class CheckAuth(APIView):
    def get(self, request, *args, **kwargs):
        if(request.user.is_authenticated):
            return JsonResponse({"is_authenticated":True})
        return JsonResponse({"is_authenticated":False})
    def post(self,request):
        logout(request)
        return Response({"Logged out"})
    
@method_decorator(csrf_exempt, name='dispatch')  # Disable CSRF protection for this view
class Logout(View):
    def post(self,request):
        logout(request)
        return JsonResponse({"Logged out":True})

