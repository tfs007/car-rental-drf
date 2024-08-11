from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Car, State, City, CarType
from .filters import CarFilter
from dealers.models import Dealer
from django.core.mail import send_mail
from django.shortcuts import redirect
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status, viewsets
from cars.serializer import CarDetailSerializer, UsedCarsSerializer, latestCarsSerializer, StateSerializer, CitySerializer, CarTypeSerializer



# Create your views here.

# def post(request):
#     data = request.data 
#     name = data.get('name')
#     message ={
#         'Message': "Hello Farzana"
#     }

#     return Response(message)
@api_view(["GET" , "POST"])
def car_list_create_api_view(request):
# def index1(request):
    if request.method == "GET":
        all = Car.objects.all()
        serailizer = CarDetailSerializer(all, many=True)
        return Response({
            "sucess" : True,
            "message": "get data",
            "data": serailizer.data
        })

    if request.method == "POST":
        serializer = CarDetailSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def index1_detail(request, pk):
    try:
        all = Car.objects.get(pk=pk)
    except Car.DoesNotExist:
        return JsonResponse({"error": {
                            "code":404,
                            "message": "Car not found!"
                        }}, status=status.HTTP_404_NOT_FOUND)

    if request.method =="GET":
        serailizer = CarDetailSerializer(all)
        return JsonResponse({
            "sucess" : True,
            "message": "get data",
            "data": serailizer.data
        })

    elif request.method == "PUT":
        serializer = CarDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        all.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)

def used_cars(request):
    if request.method == "GET":
        used_cars = Car.objects.filter(category='Used')
        serailizer = UsedCarsSerializer(used_cars, many=True)
        return JsonResponse(serailizer.data, safe=False)

def new_cars(request):
    if request.method == "GET":
        new_cars = Car.objects.filter(category='New')
        serailizer = UsedCarsSerializer(new_cars, many=True)
        return JsonResponse(serailizer.data, safe=False)

def latest_cars(request):
    if request.method == "GET":
        latest_cars = Car.objects.all().order_by('-date')
        serailizer = latestCarsSerializer(latest_cars, many=True)
        return JsonResponse({
            "sucess" : True,
            "message": "get data",
            "data": serailizer.data
        })

def index(request):
    
    new_cars = Car.objects.filter(category='New')[:6]
    used_cars = Car.objects.filter(category='Used')[:6]
    latest_cars = Car.objects.all().order_by('-date')[:5]
    all = Car.objects.all()
    myFilter = CarFilter(request.GET, queryset=all)
    all = myFilter.qs

    context = {
        'new_cars':new_cars,
        'used_cars':used_cars,
        'latest_cars':latest_cars,
        'all':all,
        'myFilter':myFilter
    }

    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')
    

def filter_results(request):
    all = Car.objects.all()
    myFilter = CarFilter(request.GET, queryset=all)
    all = myFilter.qs
    page= request.GET.get('page')
    paginator = Paginator(all, 1)
    try:
        all = paginator.page(page)
    except PageNotAnInteger:
        all = paginator.page('1')
    except EmptyPage:
        all = paginator.page(paginator.num_pages)

    page_obj=paginator.get_page(page)

    context = {
        'all':all,
        'myFilter':myFilter,
        'page_obj':page_obj
    }
    return render(request, 'filter_results.html', context)

def car_detail(request, car_id):
    cars = get_object_or_404(Car, id=car_id)

    context = {
        'cars':cars
    }
    return render(request, 'car_detail.html', context)

def inventory(request):
    inventory_cars = Car.objects.all()
    page= request.GET.get('page')
    paginator = Paginator(inventory_cars, 5)
    try:
        inventory_cars = paginator.page(page)
    except PageNotAnInteger:
        inventory_cars = paginator.page('1')
    except EmptyPage:
        inventory_cars = paginator.page(paginator.num_pages)

    page_obj=paginator.get_page(page)

    context = {
        'inventory_cars':inventory_cars,
        'page_obj':page_obj
    }
    return render(request, 'inventory.html', context )



def dealers(request):
    all_dealers = Dealer.objects.all()
    context = {
        'all_dealers':all_dealers
    }
    return render(request, 'dealers.html', context)

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            'Question from ' + name + '  Email: ' + email,
            message,
            email,
            ['']
        )
        return render(request, 'contact.html')
    else:
        return render(request, 'contact.html')

#in use
def getcardetailsView(request):
    context = {}
    if request.method == 'POST':
        data = request.POST
        data_dict = data.dict()
        print(data_dict) 
        context["carbrand"]=data_dict["carbrand"]
        # context["date"]=data_dict["date"]
        carbrand =  context["carbrand"]
        carbrand = carbrand.split(" ")
        # carbrand = "%20".join(carbrand)
        carbrand = "+".join(carbrand)
        
        nowdate =  data_dict["date"]
        print("date>>!!>> ", nowdate)
        if(nowdate!=''):
            nowdate = nowdate.split("-")
            monthnum = str(int(nowdate[1])+1)
            nowdate[1]=monthnum
            nowdate = "-".join(nowdate)
        context["date"] = nowdate
        

        # tonumber = '60122424051'
         
        all_dealers = Dealer.objects.all()
        # tonumber = {all_dealers.phone_number}
        tonumber = data_dict["tonumber"]
        # print("msg:", f"https://wa.me/{tonumber}?text=I'm%20interested%20in%20your%20car%20for%20sale")
        whatsapp_url = getwhatsappurl(tonumber,carbrand,nowdate)
        print("waurl: ",whatsapp_url)
        print("NOWDATE::", nowdate)
        print(request)
        return redirect(whatsapp_url)

       
    return render(request, 'getcardetails.html', context)

# def testdateView(request):
#     context = {}
#     if request.method == 'POST':
#         data = request.POST
#         data_dict = data.dict()
#         print(data_dict) 
#         context["date"]=data_dict["date"]
#     return render(request, 'testdate.html', context)


def getwhatsappurl(tonumber,carbrand,date):

    # tonumber = "0169477647"
    prefix = "https://api.whatsapp.com/send/?phone="
    msg = f"Hi!+I+am+interested+in+{carbrand}+on+{date}"
    url = f"{prefix}{tonumber}&text={msg}&app_absent=0"
    print("date>>", date)

    return url

def booking(request):
    # date1 = date(fromdate,todate)
    # return redirect(date1)
    return render(request, 'booking.html')

# def date(fromdate,todate):

#     count = todate - fromdate

#     return render ('booking.html' , {'count':count})


## filter search starts here...##

@api_view(["GET" , "POST"])
def state_list_create_api_view(request):

    if request.method == "GET":
        all = State.objects.all()
        serailizer = StateSerializer(all, many=True)
        return Response({
            "sucess" : True,
            "message": "get data",
            "data": serailizer.data
        })


@api_view(["GET" , "POST"])
def city_list_create_api_view(request):

    if request.method == "GET":
        all = City.objects.all()
        serailizer = CitySerializer(all, many=True)
        return Response({
            "sucess" : True,
            "message": "get data",
            "data": serailizer.data
        })


@api_view(["GET" , "POST"])
def carType_list_create_api_view(request):

    if request.method == "GET":
        all = CarType.objects.all()
        serailizer = CarTypeSerializer(all, many=True)
        return Response({
            "sucess" : True,
            "message": "get data",
            "data": serailizer.data
        })


## Car_filter search


## Filter for states & City

class CarsearchViewset(viewsets.ModelViewSet):
  serializer_class = CarDetailSerializer

  def get_queryset(self):
     car_search = Car.objects.all()
     return car_search 

  def retrieve(self, request, *args, **kwargs):

      params = kwargs
      print(params['pk'])
      params_list = params['pk'].split('-')
    #   carFilter = Car.objects.filter(Statename= params['pk']) single parameter

      carFilter = Car.objects.filter(Statename= params_list[0], City= params_list[1])
      serializer = CarDetailSerializer(carFilter, many=True)
      return Response({
            "success" : True,
            "message": "get data",
            "data": serializer.data
        }) 


## Filter for only state

class CarsearchViewsetall(viewsets.ModelViewSet):
  serializer_class = CarDetailSerializer

  def get_queryset(self):
     allcar_search = Car.objects.all()
     return allcar_search 

  def retrieve(self, request, *args, **kwargs):

      params = kwargs
      print(params['pk'])
    #   params_list = params['pk'].split('-')
      allcarFilter = Car.objects.filter(Statename= params['pk']) 

    #   carFilter = Car.objects.filter(Statename= params_list[0], City= params_list[1])
      serializer = CarDetailSerializer(allcarFilter, many=True)
      return Response({
            "success" : True,
            "message": "get data",
            "data": serializer.data
        })


##Filter for car type

class CarbrandsearchViewset(viewsets.ModelViewSet):
  serializer_class = CarDetailSerializer

  def get_queryset(self):
     carbrand_search = Car.objects.all()
     return carbrand_search 

  def retrieve(self, request, *args, **kwargs):

      params = kwargs
      print(params['pk'])
    #   params_list = params['pk'].split('-')
      carbrandFilter = Car.objects.filter(brand= params['pk']) 

    #   carFilter = Car.objects.filter(Statename= params_list[0], City= params_list[1])
      serializer = CarDetailSerializer(carbrandFilter, many=True)
      return Response({
            "success" : True,
            "message": "get data",
            "data": serializer.data
        }) 



def car_statecity(request, state_id, city_id):

    if request.method =="GET":
        carstateFilter = Car.objects.filter(state_id= state_id, city_id= city_id)
        serializer = CarDetailSerializer(carstateFilter, many=True)
        return JsonResponse({
            "success" : True,
            "message": "get data",
            "data": serializer.data
        }) 


def car_type(request, cartype_id):

    if request.method =="GET":
        cartypeFilter = Car.objects.filter(cartype_id= cartype_id)
        serializer = CarDetailSerializer(cartypeFilter, many=True)
        return JsonResponse({
            "success" : True,
            "message": "get data",
            "data": serializer.data
        })


def car_filter_object(state_id,city_id,cartype_id):
    print(f"state:{state_id}; city:{city_id}; type:{cartype_id}")
    if(state_id==0 and city_id ==0 and cartype_id==0):
        print(1)
        return  Car.objects.all()
    if (state_id==0 and city_id ==0):
        print(2)
        return Car.objects.filter(cartype_id= cartype_id)
    if(city_id==0 and cartype_id==0):
        print(3)
        return Car.objects.filter(state_id = state_id)
    if(state_id==0 and cartype_id==0):
        print(4)
        return Car.objects.filter(city_id= city_id)
    if(state_id==0):
        print(5)
        return Car.objects.filter(city_id= city_id, cartype_id= cartype_id)
    if(city_id==0):
        print(6)
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        return Car.objects.filter(state_id = state_id, cartype_id= cartype_id)
    if(cartype_id==0):
        print(7)
        return Car.objects.filter(state_id = state_id, city_id= city_id)
    else:
        print(8)
        return Car.objects.filter(state_id = state_id,city_id= city_id, cartype_id= cartype_id)



def car_typeall(request, state_id, city_id,cartype_id):
    
    if request.method =="GET":
        print(f"state:{state_id}; city:{city_id}; type:{cartype_id}")
        cartypeFilter = car_filter_object(state_id,city_id,cartype_id)
        serializer = CarDetailSerializer(cartypeFilter, many=True)
        return JsonResponse({
            "success" : True,
            "message": "get data",
            "data": serializer.data
        })