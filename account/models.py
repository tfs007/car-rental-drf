from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    # is_carDealer = models.BooleanField(default=False)

class Customer(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
    	return self.name





# class CarDealer(models.Model):
#     # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     phone_number = models.CharField(max_length=15)
#     picture = models.ImageField(upload_to='images')
#     email = models.CharField(max_length=50)


#     def __str__(self):
#     	return self.user.username
