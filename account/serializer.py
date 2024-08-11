from rest_framework import serializers
from account.models import Customer
from rest_framework.validators import UniqueValidator


class CustomerSerializer(serializers.ModelSerializer):


    # class Meta:
    #     model = Customer
    #     fields = "__all__"

        email = serializers.EmailField(
        required = True,
        validators = [UniqueValidator(queryset=Customer.objects.all())]
    ) 
       
        class Meta:
            model = Customer
            fields = "__all__"

        

        
