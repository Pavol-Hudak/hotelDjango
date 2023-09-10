from rest_framework import serializers
from . models import GuestModel

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestModel
        fields = ('id',
                  'first_name',
                  'middle_name',
                  'last_name',
                  'email',
                  'date_of_birth',
                  'password',
                  )
        
class CreateGuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestModel
        fields = ('id', 'first_name', 'middle_name', 'last_name', 'date_of_birth', 'email','password')

'''class LoginGuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('email','password')'''
