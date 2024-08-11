from django.urls import path
from cars.views import *
from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include

router = DefaultRouter()
router.register('car_search', CarsearchViewset, basename='car_search')
router.register('allcar_search', CarsearchViewsetall, basename='allcar_search')
router.register('carbrand_search', CarbrandsearchViewset, basename='carbrand_search')


urlpatterns = [
    ## all cars
    path("cars/",car_list_create_api_view, name="car-list"),
    # path('cars/', index1),
    ##car detail by id
    path('cars/<int:pk>/', index1_detail),

    path('carfilter/<int:state_id>/<int:city_id>/', car_statecity),
    ##
    path('carfilter/<int:state_id>/<int:city_id>/<int:cartype_id>/', car_typeall),
    ##
    # path('carfilter/<int:cartype_id>/', car_type),
    path("states/",state_list_create_api_view, name="state-list"),
    path("city/",city_list_create_api_view, name="city-list"),
    path("cartype/",carType_list_create_api_view, name="carType-list"),

    url('',include(router.urls))
    
]