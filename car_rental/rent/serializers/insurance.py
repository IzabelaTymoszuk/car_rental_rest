from rest_framework import serializers, fields
from ..models.insurance import Insurance, TYPE_INSURANCE
from datetime import date
from rest_framework import fields
from ..models.car import Car


class InsuranceSerializer(serializers.ModelSerializer):
    type_of_insurance = fields.MultipleChoiceField(choices=TYPE_INSURANCE)
    end_date = fields.DateField(input_formats=['%Y-%m-%d', 'iso-8601',])

    class Meta:
        model = Insurance

        fields = ['insurance_status', 'insurance_company', 'end_date', 'type_of_insurance',
                  'worth_of_insurance', 'insurance_number', 'car']
        read_only_fields = ['end_date']


    def validate_type_of_insurance(self, value):

        """
        Validation of type of insurance.
        Checks if the car has compulsory OC insurance.
        """

        if 'OC' not in value:
            raise serializers.ValidationError("The car must have OC")
        return value

    def validate(self, data):

        """
        Validation of car data and insurance data relation.
        Checks that if the car is leased, the car has a full insurance too.
        """

        car_id = data['car'].id
        leasing = 'L'
        insurance = data['type_of_insurance']
        car_qs = Car.objects.filter(id=car_id)
        if not car_qs.exists():
            raise serializers.ValidationError('This car not exist...!')

        car = car_qs[0]
        car.status = False
        if car.way_of_purchase == leasing and insurance != {'AC', 'OC', 'NWW'}:
            raise serializers.ValidationError("If you bought a car in leasing, you must have full insurance.")

        if data['end_date'] < date.today() and data['insurance_status'] == True:
            raise serializers.ValidationError("Are you sure this car has insurance?")

        return data


