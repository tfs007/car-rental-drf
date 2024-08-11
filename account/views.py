from django.shortcuts import render,redirect
from django.contrib.auth import login
# Create your views here.


from django.views.generic import CreateView

# from .forms import CustomerSignUpForm,CarDealerSignUpForm
from .models import User,Customer
# ,CarDealer

from rest_framework import generics
from rest_framework import mixins
from rest_framework.decorators import api_view
from dealers.models import Dealer
from account.serializer import CustomerSerializer
from rest_framework import status
from rest_framework.response import Response


# def SignUp(request):
# 	return render(request,'register.html')

# class CustomerSignUpView(CreateView):
#     model = User
#     form_class = CustomerSignUpForm
#     template_name = 'signup.html'

#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'customer'
#         return super().get_context_data(**kwargs)

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         #return redirect('main')

# class CarDealerSignUpView(CreateView):
#     model = User
#     form_class = CarDealerSignUpForm
#     template_name = 'signup.html'

#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'carDealer'
#         return super().get_context_data(**kwargs)

#     def form_valid(self, form):
#         user = form.save()
#         #login(self.request, user)
#         #return redirect('main')



    
# @api_view(["GET" , "POST"])
# def Customer_list_create_api_view(request):
# # def index1(request):
#     if request.method == "GET":
#         all = Customer.objects.all()
#         serailizer = CustomerSerializer(all, many=True)
#         return Response({
#             "sucess" : True,
#             "message": "get data",
#             "data": serailizer.data
#         })

#         if request.method == "POST":
#            serializer = CustomerSerializer(data=request.data)
        
#            if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET" , "POST"])
def Customer_list_create_api_view(request):
# def index1(request):
   
    if request.method == "GET":
        all = Customer.objects.all()
        serailizer = CustomerSerializer(all, many=True)
        return Response({
            "sucess" : True,
            "message": "get data",
            "data": serailizer.data
        })

    if request.method == "POST":
        serializer = CustomerSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def customer_filter_object(email):
    #print(f"email:{email}")
    return Customer.objects.filter(email = email)


@api_view(["GET" , "POST"])
def customer_type(request, email):
    
    if request.method =="GET":
        #print(f"email:{email};")
        CustomerFilter = customer_filter_object(email)
        serializer = CustomerSerializer(CustomerFilter, many=True)
        return Response({
            "success" : True,
            "message": "get data",
            "data": serializer.data
        })