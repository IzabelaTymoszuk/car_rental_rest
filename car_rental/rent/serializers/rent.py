from rest_framework import serializers
from ..models.rent import Rent, Car
from datetime import date


class RentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = ['start_rent', 'end_rent', 'deposit', 'number_of_day', 'amount', 'car']

    def validate(self, data):

        """
        Validation of car's status data and rent date.
        Checks if a rent date is possible.
        """

        if data['start_rent'] > data['end_rent'] or data['end_rent'] <= date.today() or data[
            'start_rent'] < date.today():
            raise serializers.ValidationError('The date is not correct.')

        """Checks if car is available."""

        car_id = data['car'].id
        car_qs = Car.objects.filter(id=car_id)
        car = car_qs[0]
        if car.status != 'A':
            raise serializers.ValidationError('You can not rent a car that is not available.')

        return data
