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
                  'date_of_birth',
                  'account_created',
                  'membership'
                  )