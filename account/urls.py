from django.urls import path
from .views import Customer_list_create_api_view, customer_type
# SignUp,CustomerSignUpView,CarDealerSignUpView,
urlpatterns = [
# path('signup/',SignUp,name='signup'),
# path('account/signup/customer/', CustomerSignUpView.as_view(), name='Customer_signup'),
# path('account/signup/carDealer/', CarDealerSignUpView.as_view(), name='CarDealer_signup'),
 
path("account/customer/",Customer_list_create_api_view,name="customer-list"),
path("account/customer/<str:email>/",customer_type)



]