from django.contrib import admin
from booking.models import Booking,CarBooking

# Register your models here.


class BookingAdmin(admin.ModelAdmin):
    list_display = ('car','customer_first_name','customer_last_name','email','phone_number','address','city','pickup_date','dropoff_date','select_time','pick_up_location','drop_off_location'
)
    list_per_page = 4
    search_fields = ('customer_first_name','car')

admin.site.register(Booking,BookingAdmin)
admin.site.register(CarBooking)