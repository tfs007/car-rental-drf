from django.db import models
import datetime
from cars.models import Car
from django.utils import timezone
#from django.core.exceptions import ValidationError
from django.db.models import Q, F
from django.contrib.auth.models import User
from datetime import date
from account.models import Customer

today = timezone.now

# Create your models here.
#...
class Booking(models.Model):
    car = models.ForeignKey(Car, on_delete=models.DO_NOTHING)
    # car = models.CharField(max_length=10,default=1)
    customer_first_name = models.CharField(max_length=50,default="XXXX")
    customer_last_name = models.CharField(max_length=50,default="XXXX")
    email = models.CharField(max_length=50,unique=True,default="test@gmail.com")
    phone_number = models.CharField(max_length=15,null=True,default=None)
    address = models.CharField(max_length=200,default="XXXX")
    city = models.CharField(max_length=100,default="XXXX")
    #YEAR_CHOICES = [(r,r) for r in range(2005, datetime.date.today().year+1)]
    #year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    pickup_date = models.DateField(default=today)
    dropoff_date = models.DateField(default=today)
    #end_date = models.DateField()
    select_time=models.TimeField(default=timezone.now)
    pick_up_location = models.CharField(max_length=100)
    drop_off_location = models.CharField(max_length=100)

    def __str__(self):
        return self.customer_first_name

    # def clean(self):
    #     if self.start_date > self.end_date:
    #         raise ValidationError('Start date should be before end date')
    #     return super().clean()

    # class Meta:
    #     constraints = [
    #         models.CheckConstraint(
    #             check=Q(start__lte=F('end')),
    #             name='start_before_end')
            
    #  ]

    
class CarBooking(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    car_id = models.ForeignKey(Car, on_delete=models.DO_NOTHING)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15,null=True,default=None)
    carpickup_date = models.DateTimeField(blank=True)
    cardropoff_date = models.DateTimeField(blank=True)
    pick_up_location = models.CharField(max_length=100)
    drop_off_location = models.CharField(max_length=100)

    def __str__(self):
        return self.email
