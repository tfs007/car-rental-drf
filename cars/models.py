from django.db import models
import datetime
from dealers.models import Dealer
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image
from PIL import ImageOps

# Create your models here.

class State(models.Model):
    
    states = (
            ('Kuala Lumpur','Kuala Lumpur'),
            ('Selangor','Selangor'),
            ('Pahang','Pahang'),
            ('Perak','Perak')
            
        )
    Statename = models.CharField(max_length=50, choices=states)
    

    def __str__(self):
        return self.Statename


class City(models.Model):
    Statename = models.ForeignKey(State, on_delete=models.DO_NOTHING)
    city = (
            ('KL Sentral','KL Sentral'),
            ('KLCC','KLCC'),
            ('Masjid Jamek','Masjid Jamek'),
            ('Kajang','Kajang'),
            ('Bangi','Bangi'),
            ('Brinchang','Brinchang'),
            ('Tanah Rata','Tanah Rata'),
            ('Lumut','Lumut'),
            ('Ipoh','Ipoh'),
            
        )

    City = models.CharField(max_length=50, choices=city)

    def __str__(self):
        return self.City


class CarType(models.Model):
    
    type = (
            ('Sports Car','Sports Car'),
            ('Luxury Sedan','Luxury Sedan'),
            ('Hatchback','Hatchback'),
            ('MPV','MPV'),
            ('SUV','SUV'),
            ('Hybrid Car','Hybrid Car'),
            ('Electric Car','Electric Car')
        )
    Cartype = models.CharField(max_length=50, choices=type)

    def __str__(self):
        return self.Cartype


class Car(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.DO_NOTHING)
    state_id = models.ForeignKey(State, on_delete=models.DO_NOTHING)
    city_id = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    brand = models.CharField(max_length=100)
    cartype_id = models.ForeignKey(CarType, on_delete=models.DO_NOTHING)
    image_main = models.ImageField(upload_to='images')
    image1 = models.ImageField(upload_to='images', blank=True)
    image2 = models.ImageField(upload_to='images', blank=True)
    image3 = models.ImageField(upload_to='images', blank=True)
    image4 = models.ImageField(upload_to='images', blank=True)
    image5 = models.ImageField(upload_to='images', blank=True)

    miles = models.IntegerField(blank=True, null=True)
    TRANSMISSION = (
                ('Manual','Manual'),
                ('Automatic','Automatic')
    )

    transmission = models.CharField(max_length=50, choices=TRANSMISSION)
    YEAR_CHOICES = [(r,r) for r in range(2005, datetime.date.today().year+1)]
    year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    CarEngine = (
        ('1.6cc','1.6cc'),
        ('1.8cc','1.8cc'),
        ('2.0cc','2.0cc'),
        ('3.0cc','3.0cc'),
        ('4.0cc','4.0cc')
        
    )
    car_engine_size = models.CharField(max_length=50, default = "1.6cc", choices=CarEngine)
    power = models.IntegerField()
    fuel = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    date = models.DateField()
    Availablity = (
        ('Available','Available'),
        ('Not Available','Not Available')
    )
    availablity = models.CharField(max_length=50, default = "Available", choices=Availablity)

    def __str__(self):
        return self.brand

    def get_absolute_url(self):
        return reverse('car_detail', kwargs = {
                        'car_id':self.id
        })

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image_main.path)
        target_dim = (400,400)
        im_new = ImageOps.fit(img, target_dim)
        im_new.save(self.image_main.path,"JPEG")

    


###Filter search purpose starts here.....###





