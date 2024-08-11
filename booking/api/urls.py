from django.urls import path
from booking.api.views import booking_list_create_api_view,bookingdetail_create_api_view,carbookingdetail_list_create_api_view,carbooking_list_create_api_view,CarBooking_type

urlpatterns = [
path("booking/",carbooking_list_create_api_view, name="booking-list"),
# path("booking/",booking_list_create_api_view, name="booking-list"),
path("booking/<int:pk>/",bookingdetail_create_api_view, name="booking-list-bookingid"),
path("booking/car/<int:carid>/",carbookingdetail_list_create_api_view, name="booking-list-carid"),
path("booking/<str:email>/",CarBooking_type)
]