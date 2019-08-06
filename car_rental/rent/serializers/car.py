from rest_framework import serializers, fields
from rest_framework.relations import HyperlinkedIdentityField
from ..models.car import Car, FUEL
from rest_framework.validators import UniqueValidator


class CarSerializer(serializers.HyperlinkedModelSerializer):
    fuel_types = fields.MultipleChoiceField(choices=FUEL)

    def validate_year_of_manufacture(self, value):
        if value < 1995:
            raise serializers.ValidationError("This car is too old")
        return value

    def validate_VIN(self, value):
        if len(value) < 17:
            raise serializers.ValidationError("VIN have to have 17 characters.")
        return value

    class Meta:
        model = Car
        fields = ['id', 'status', 'make', 'model', 'price_per_day', 'body_styles', 'way_of_purchase', 'fuel_types',
                  'color', 'engine', 'VIN', 'transmission', 'year_of_manufacture']
