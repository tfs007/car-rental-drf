# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.db import transaction

# from .models import Customer, User,CarDealer

# class CustomerSignUpForm(UserCreationForm):
#     email=forms.EmailField(required=True)
  
#     class Meta(UserCreationForm.Meta):
#         model = User

#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.email=self.cleaned_data.get('email')
#         user.is_customer = True
#         user.save()
#         customer = Customer.objects.create(user=user)
#         customer.email=self.cleaned_data.get('email')
#         customer.city=self.cleaned_data.get('city')
#         return user


# class CarDealerSignUpForm(UserCreationForm):
#     email=forms.CharField(required=True)
#     phone_number=forms.CharField(required=True)
#     picture = forms.ImageField(required=False)
    
#     class Meta(UserCreationForm.Meta):
#         model = User

#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_carDealer = True
#         user.save()
#         carDealer = CarDealer.objects.create(user=user)
#         carDealer.phone_number=self.cleaned_data.get('phone_number')
#         carDealer.email=self.cleaned_data.get('email')
#         carDealer.picture = self.cleaned_data.get('picture')
#         carDealer.save()

#         return carDealer