from django.urls import path
# from CarDealer.api.views import CarDealerListCreateAPIView
from CarDealer.api.views import Car_dealer_list_create_api_view

urlpatterns = [
    path("CarDealer/", 
         Car_dealer_list_create_api_view, 
         name="car-list")

]