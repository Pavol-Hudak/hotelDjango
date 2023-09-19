from django.contrib import admin

from .models import GuestModel, RoomModel, ReservationModel

admin.site.register(GuestModel)
admin.site.register(RoomModel)
admin.site.register(ReservationModel)

# Register your models here.
