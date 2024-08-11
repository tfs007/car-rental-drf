"""CarDealer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from cars.admin import site
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from cars import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# admin.site = site
# admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('inventory/', views.inventory, name="inventory"),
    path('dealers/', views.dealers, name="dealers"),
    path('contact/', views.contact, name="contact"),
    path('<int:car_id>', views.car_detail, name="car_detail"),
    path('filter_results', views.filter_results, name="filter_results"),
    path("getcardetail/", views.getcardetailsView, name="getcardetail"),
    path("api/", include("CarDealer.api.urls")),
    path("api/v1/", include("cars.api_urls")),
    path('usedcar/', views.used_cars, name="used_cars"),
    path('newcar/', views.new_cars, name="new_cars"),
    path('latestcar/', views.latest_cars, name="latest_cars"),
    #path('booking/', views.booking, name = "booking"),
    # path('booking/', views.booking, name = "booking"),
    path("api/", include("booking.api.urls")),
    path('api/token',TokenObtainPairView.as_view()),
    path('api/token/refresh',TokenRefreshView.as_view()),
    path('account/', include('account.urls')),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
