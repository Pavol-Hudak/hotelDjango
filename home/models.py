from django.db import models
from datetime import datetime
import random

# Create your models here.
NAME_LENGTH = 20



def generateMemberId():
    current_time = (datetime.now()).strftime("%H%M%S")
    random_id = random.randint(1000,9999)
    combine_id = (f"{current_time}{random_id}")
    member_id = ''.join(random.sample(combine_id, len(combine_id)))
    return member_id


class Guest(models.Model):
    member_id = models.IntegerField(default=generateMemberId)
    first_name = models.CharField(max_length=NAME_LENGTH)
    middle_name = models.CharField(max_length=NAME_LENGTH)
    last_name = models.CharField(max_length=NAME_LENGTH)
    date_of_birth = models.DateField()
    account_created = models.DateField(auto_now_add=True)
    membership = models.BooleanField(null=False, default=False)
