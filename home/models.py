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


'''class Guest(models.Model):
    member_id = models.IntegerField(default=generateMemberId)
    first_name = models.CharField(max_length=NAME_LENGTH)
    middle_name = models.CharField(max_length=NAME_LENGTH)
    last_name = models.CharField(max_length=NAME_LENGTH)
    email = models.EmailField(max_length=254,default='')
    date_of_birth = models.DateField()
    account_created = models.DateTimeField(auto_now_add=True)
    membership = models.BooleanField(null=False, default=False)
    password = models.CharField(default='',max_length=254,validators=[MinLengthValidator(PASSWORD_MIN_LENGTH,'Password must be at least 8 characters long')])
    current_session = models.CharField(default='',max_length=254)
'''

class GuestManager(BaseUserManager):
    def create_guest(self, email, first_name, middle_name, last_name, date_of_birth,  password):
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
    email = models.EmailField()  # Define the 'email' field
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    
    
    # Specify the 'email' field as the username field
    USERNAME_FIELD = 'email'
    
    # Specify other fields that are required when creating a user
    REQUIRED_FIELDS = ['first_name', 'last_name', 'date_of_birth']
    objects = GuestManager()
    