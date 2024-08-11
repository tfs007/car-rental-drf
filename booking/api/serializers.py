from rest_framework import serializers
from booking.models import Booking, CarBooking
from cars.serializer import CarDetailSerializer
import datetime
from django.utils import timezone
from cars.models import Car

class BookingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Booking
        #fields = "__all__"

        fields = [
            'car',
            'customer_first_name',
            'customer_last_name',
            'email',
            'phone_number',
            'address',
            'city',
            'pickup_date',
            'dropoff_date',
            'select_time',
            'pick_up_location',
            'drop_off_location'
        ]





class CarBookingSerializer(serializers.ModelSerializer):
    # car = CarDetailSerializer(read_only=True)
    # brand = serializers.SlugRelatedField(queryset=CarBooking.objects.all(), slug_field='brand', write_only=True)

    # class Meta:
    #     model = Car 
    #     fields = [
    #         'brand',
    #         'car_id'
    #     ]
        model = Booking
        # fields = "__all__"
        # model = Booking
        fields = [
            'Start_date',
            'End_date',
            'select_time',
        ]
        # brand = serializers.CharField(max_length=100)
        # start_date = serializers.DateField()
        # end_date = serializers.DateField()
        # pickup_time=serializers.TimeField()

class CarBookingSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = CarBooking
        fields = "__all__"