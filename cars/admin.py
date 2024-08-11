from django.contrib import admin
from .models import Car, State, City, CarType
from booking.models import Booking
from .models import Dealer
from django.contrib.auth.admin import UserAdmin


# Register your models here.
admin.site.register(Car)
admin.site.register(State)
admin.site.register(City)
admin.site.register(CarType)


