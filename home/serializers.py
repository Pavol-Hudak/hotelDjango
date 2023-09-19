from rest_framework import serializers
from . models import GuestModel, RoomModel, ReservationModel

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
                  'account_created',
                  'is_staff',
                  'is_superuser',
                  'is_active'
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

class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomModel
        fields = ('id','capacity','room_type','price','description')
        
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationModel
        fields = ('id','guest_id','room_id','res_from','res_until')

class CreateReservationSerializer(serializers.Serializer):
    persons = serializers.IntegerField()
    checkInSearch = serializers.DateField()
    checkOutSearch = serializers.DateField()