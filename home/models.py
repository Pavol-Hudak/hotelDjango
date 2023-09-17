from django.db import models
from datetime import datetime
import random
from django.core.validators import MinLengthValidator, validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.
NAME_LENGTH = 20
PASSWORD_MIN_LENGTH = 2



def generateMemberId():
    current_time = (datetime.now()).strftime("%H%M%S")
    random_id = random.randint(1000,9999)
    combine_id = (f"{current_time}{random_id}")
    member_id = ''.join(random.sample(combine_id, len(combine_id)))
    return member_id

class GuestManager(BaseUserManager):
    def create_guest(self, email, first_name, middle_name, last_name, date_of_birth, password):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError("Invalid email address")
        guest = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            middle_name = middle_name,
            last_name = last_name,
            date_of_birth = date_of_birth,
        )
        print(email)
        if password:
            guest.set_password(password)
        guest.save(using=self._db)
        return guest

class GuestModel(AbstractBaseUser):
    email = models.EmailField(unique=True)  # Define the 'email' field
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    member_id = models.CharField(default=generateMemberId, max_length=10)
    account_created = models.DateTimeField(auto_now=True)
    
    # Specify the 'email' field as the username field
    USERNAME_FIELD = 'email'
    
    # Specify other fields that are required when creating a user
    REQUIRED_FIELDS = ['first_name', 'last_name', 'date_of_birth']
    objects = GuestManager()


class RoomModel(models.Model):
    ROOM_TYPES = [
        ("D", "Double"),
        ("K", "King"),
        ("S", "Suite"),
        ("P", "Presidential"),
    ]
    capacity = models.IntegerField(default=2)
    room_type = models.CharField(max_length=254,default="Suite")
    price = models.FloatField(default=0.0)
    description = models.TextField(max_length=254)

'''class ReservedRoomModel(models.Model):
    room_id = models.ForeignKey(RoomModel, on_delete=models.CASCADE)

class ReservationModel(models.Model):
    guest_id = models.ForeignKey(GuestModel, on_delete=models.CASCADE)
    room_id = models.ForeignKey(ReservedRoomModel, on_delete=models.CASCADE)
    res_from = models.DateField()
    res_until = models.DateField()'''
        


    