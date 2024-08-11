from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from booking.models import Booking, CarBooking
from cars.models import Car
from booking.api.serializers import BookingSerializer, CarBookingSerializer
from rest_framework import serializers
from cars.serializer import CarDetailSerializer



@api_view(["GET" , "POST"])
def booking_list_create_api_view(request):
    
    if request.method == "GET":
       booking = Booking.objects.all()
       serializer = BookingSerializer(booking, many=True)
       return Response(serializer.data)

    if request.method == "POST":
        rdata = request.data.copy()
        ####
        rdata = dict(rdata)
        rdata_l = [x[0] for x in rdata.values()]
        keys = list(rdata.keys())
        new_rdata = dict(zip(keys,rdata_l))
        rdata = new_rdata

        ####
        # rdata = dict(rdata)
        print("<<<<<", rdata)
        # return Response({"message":"test"})
        print("Rdata car::", rdata['car'])
        rdata_car = int(rdata['car'])
        rdata['car'] = rdata_car

        s = rdata["select_time"];
        print("select time", s)
        ss = s.split("-")

        def getnum(x):
            if(len(x)==1):
                return "0"+x
            else:
                return x
        
        ss2 = [getnum(x) for x in ss]
        ss2.append("00")
        Time2 = ":".join(ss2)

        
        print(f"time2 : {Time2}")
        rdata['select_time']=Time2
        print(rdata)
        ###############
        def rev(x):
            x_split= x.split("/")
            x_split.reverse()
            return "-".join(x_split)
        #date_list = rdata['select_date'].split('-') 
        #print('date list', date_list) 

        # split_date = [rev(x).replace(" ","") for x in date_list]
        # print('splitdate',split_date)
        # pickup_date2= split_date[0]
        # dropoff_date2 =split_date[1]
        # rdata['pickup_date'] = pickup_date2
        # rdata['dropoff_date'] = dropoff_date2
        # print('pickup_date2:',pickup_date2)
        #############
        #print('pickup_date:',rdata['pickup_date'])
        #rdata2= {'car':2,'customer_first_name':'test customer'}


        # def rev(x):
        #     x_split= x.split(",")
        #     x_split.reverse()
        #     return "-".join(x_split)
        # date_list = rdata['First_date'].split('-') 
        # print('date list', date_list)


        booking = Booking.objects.create( 
            car_id= rdata['car'],
            customer_first_name=rdata['customer_first_name'],
            customer_last_name=rdata['customer_last_name'],
            email=rdata['email'],
            phone_number=rdata['phone_number'],
            address=rdata['address'],
            city=rdata['city'],
            pick_up_location=rdata['pick_up_location'],
            drop_off_location=rdata['drop_off_location'],
            select_time=rdata['select_time'],
            pickup_date=rdata['Start_date'],
            dropoff_date=rdata['End_date'],

        )
        booking.save()
        return Response({'message':'success'})

        ##############
        #################
        # serializer = BookingSerializer(data=rdata)#rdata
        # serializer = BookingSerializer(data=rdata2)#rdata

        # print("<<<<<<<<<<<<<<<<<<valid",serializer.is_valid())
        # print("")
        # if serializer.is_valid():
        #     print("sdata,,,,,,,,,,,,,,,,,,",serializer.data)
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ! The function name should not contain list as it will return only one booking, not a list.
@api_view(["GET" , "POST"])
def bookingdetail_create_api_view(request, pk):
    try:
        all = Booking.objects.get(pk=pk)
    except Booking.DoesNotExist:
        return Response({"error": {
                            "code":404,
                            "message": "Booking not found!"
                        }}, status=status.HTTP_404_NOT_FOUND)

    if request.method =="GET":
        serializer = BookingSerializer(all)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        all.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET" , "POST"])
def carbookingdetail_list_create_api_view(request, carid):
    try:
        # all = Car.objects.get(pk=pk)
        
        all = Booking.objects.filter(car__id=carid) #Note that this is a list.~Talat

        # serializer= BookingSerializer(all, many=True)
        # print("data>>: ", serializer.data)
        # return Response(serializer.data)
        # data = serializers.serialize('json', all)
        # data=serializers.serialize('json',all)
        print("all>>> ", all)
        # return Response(data)
        
    except Booking.DoesNotExist:
        return Response({"error": {
                            "code":404,
                            "message": "Booking not found!"
                        }}, status=status.HTTP_404_NOT_FOUND)

    if request.method =="GET":
        serializer = BookingSerializer(all,many=True)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ",serializer)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        all.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





####Problem#####

@api_view(["GET" , "POST"])
def carbooking_list_create_api_view(request):
    print("!!!!!!!!!!!!!!!!!!!!!")
    print(request.method)
    
    
    if request.method == "GET":
       print("<<<<<<<<<<<<get>>>>>>>>>>>>")
       carbooking = CarBooking.objects.all()
       serializer = CarBookingSerializer(carbooking, many=True)
       return Response(serializer.data)

    if request.method == "POST":
        print("Post>>>>>>>>>>>>>>>>>>>>")
        print(request.data)
        print(type(request.data))
        serializer = CarBookingSerializer(data=request.data)
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<", serializer)
        if serializer.is_valid():
            print("<<<<<<<<<<Valid>>>>>>>>>>>")
            serializer.save()
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@");
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

############################



def CarBooking_filter_object(email):
    #print(f"email:{email}")
    return CarBooking.objects.filter(email = email)


@api_view(["GET" , "POST"])
def CarBooking_type(request, email):
    
    if request.method =="GET":
        #print(f"email:{email};")
        CarBookingFilter = CarBooking_filter_object(email)
        serializer = CarBookingSerializer(CarBookingFilter, many=True)
        bookings = [Car.objects.get(id=x['car_id']) for x in serializer.data]
        bookings = [ CarDetailSerializer(x).data for x in bookings]
        print("@@@@@@@@@@@@@@@@@@@@",bookings)
        print(serializer)
        return Response({
            "success" : True,
            "message": "get data",
            "data": serializer.data,
            "cardata": bookings
        })