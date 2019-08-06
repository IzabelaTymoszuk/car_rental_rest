from rest_framework import serializers
from ..models.rent import Rent


class RentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rent
        fields = ['start_rent', 'end_rent', 'deposit', 'number_of_day', 'amount', 'car']
