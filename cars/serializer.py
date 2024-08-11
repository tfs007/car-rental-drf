from rest_framework import serializers
from cars.models import Car, State, City, CarType

class CarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"

class UsedCarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('category')
        fields = "__all__"

class NewCarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('category')
        fields = "__all__"


class latestCarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('date')
        fields = "__all__"


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = "__all__"

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"

class CarTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarType
        fields = "__all__"