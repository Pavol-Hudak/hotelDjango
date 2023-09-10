from rest_framework import serializers
from . models import Guest

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('id',
                  'member_id',
                  'first_name',
                  'middle_name',
                  'last_name',
                  'email',
                  'date_of_birth',
                  'account_created',
                  'membership',
                  'password',
                  'current_session'
                  )
        
class CreateGuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('first_name','middle_name','last_name','date_of_birth','email','password')

class LoginGuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('email','password')

class CurrentSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('current_session')