from django.contrib import admin

# Register your models here.
from account.models import User,Customer


admin.site.register(User)

admin.site.register(Customer)

# admin.site.register(CarDealer)
