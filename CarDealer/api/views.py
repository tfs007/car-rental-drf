from rest_framework import generics
from rest_framework import mixins
from rest_framework.decorators import api_view
from dealers.models import Dealer
from CarDealer.api.serializers import CarSerializer
from rest_framework import status
from rest_framework.response import Response

# class CarDealerListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Dealer.objects.all().order_by("id")
#     serializer_class = CarSerializer
#     return Response({
#             "sucess" : True,
#             "message": "get data",
#             "data": serailizer.data
#         })
    
@api_view(["GET" , "POST"])
def Car_dealer_list_create_api_view(request):
# def index1(request):
    if request.method == "GET":
        all = Dealer.objects.all().order_by("id")
        serailizer = CarSerializer(all, many=True)
        return Response({
            "sucess" : True,
            "message": "get data",
            "data": serailizer.data
        })