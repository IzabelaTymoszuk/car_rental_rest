from rest_framework import serializers, fields
from ..models.user import RenterUser, DRIVING_LICENSE_PERMISSION


class RenterSerializer(serializers.ModelSerializer):
    categories_of_vehicles = fields.MultipleChoiceField(choices=DRIVING_LICENSE_PERMISSION)

    class Meta:
        model = RenterUser
        fields = ['id', 'first_name', 'last_name', 'categories_of_vehicles', 'driving_license_number',
                  'company', 'PESEL']