from rest_framework import serializers, fields
from ..models.insurance import Insurance, TYPE_INSURANCE


class InsuranceSerializer(serializers.ModelSerializer):
    type_of_insurance = fields.MultipleChoiceField(choices=TYPE_INSURANCE)

    def validate_type_of_insurance(self, value):
        if 'OC' not in value:
            raise serializers.ValidationError("The car must have OC")
        return value

    class Meta:
        model = Insurance
        fields = ['insurance_status', 'insurance_company', 'end_date', 'type_of_insurance',
                  'worth_of_insurance', 'insurance_number', 'car']