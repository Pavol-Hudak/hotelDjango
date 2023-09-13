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
                  'member_id',
                  'account_created'
                  )
        
class CreateGuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestModel
        fields = ('id', 'first_name', 'middle_name', 'last_name', 'date_of_birth', 'email','password')

class LoginGuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestModel
        fields = ('email','password')

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128)
