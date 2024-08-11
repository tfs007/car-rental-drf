from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Dealer(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, default="0123456667")
    picture = models.ImageField(upload_to='images')
    description = models.TextField()
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name
