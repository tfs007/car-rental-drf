from rest_framework import serializers
from dealers.models import Dealer


class CarSerializer(serializers.ModelSerializer):


    class Meta:
        model = Dealer
        fields = "__all__"