from rest_framework import serializers, fields
from ..models.car import Car, FUEL
from datetime import date


class CarSerializer(serializers.ModelSerializer):
    fuel_types = fields.MultipleChoiceField(choices=FUEL)

    def validate_year_of_manufacture(self, value):

        """
        Validation of year of manufacture.
        Checks if the car has been manufactured.
        """

        if value < 1903:
            raise serializers.ValidationError("This car is too old.")
        return value

    def validate_VIN(self, value):

        """
        Validation of length of VIN.
        The length of the VIN must be 17 characters.
        """

        if len(value) < 17:
            raise serializers.ValidationError("VIN have to have 17 characters.")
        return value

    def validate(self, data):

        """
        Validation of car's year of manufacture data.
        Checks that if car will be produced in the future, has the status set to F
        """

        if data['year_of_manufacture'] > date.today().year and data['status'] != 'F':
            raise serializers.ValidationError("If your car will be manufactured in the future, you should indicate this")
        return data

    class Meta:
        model = Car
        fields = ['id', 'status', 'make', 'model', 'price_per_day', 'body_styles', 'way_of_purchase', 'fuel_types',
                  'color', 'engine', 'VIN', 'transmission', 'year_of_manufacture']