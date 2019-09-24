from rest_framework.test import APITestCase
from ...models.insurance import Insurance
from ...models.car import Car
from ...serializers.insurance import InsuranceSerializer
import datetime


class InsuranceSerializerTests(APITestCase):
    def setUp(self):
        self.car_attributes = {
            'status': 'A',
            'make': 'Citroen',
            'model': 'C4',
            'price_per_day': 30,
            'body_styles': 'C',
            'way_of_purchase': 'L',
            'fuel_types': ['P'],
            'color': 'Red',
            'engine': '1.4',
            'VIN': 'ASGH654HJK9835679',
            'transmission': 'M',
            'year_of_manufacture': 2016,
            'next_review_date': datetime.date(2019, 12, 30)
        }
        self.car = Car.objects.create(**self.car_attributes)

        self.insurance_attributes = {
            'insurance_status': True,
            'insurance_company': 'AXA',
            'end_date': datetime.date(2019, 9, 30),
            'type_of_insurance': ['OC', 'AC', 'NWW'],
            'worth_of_insurance': 300000,
            'car': self.car,
            'insurance_number': 'JHVS675/76576/19'
        }

        self.serializer_data = {
            'insurance_status': True,
            'insurance_company': 'PZU',
            'end_date': datetime.date(2019, 9, 30),
            'type_of_insurance': ['OC', 'AC'],
            'worth_of_insurance': 300000,
            'car': self.car,
            'insurance_number': 'JHVS675/76576/19'
        }

        self.insurance = Insurance.objects.create(**self.insurance_attributes)
        self.insurance_serializer = InsuranceSerializer(instance=self.insurance)

    def test_contains_expected_fields(self):
        data = self.insurance_serializer.data
        self.assertEqual(set(data.keys()), set(['insurance_status', 'insurance_company', 'end_date',
                                                'type_of_insurance', 'worth_of_insurance', 'insurance_number', 'car']))

    def test_validate_type_of_insurance(self):
        self.insurance_attributes['type_of_insurance'] = ['AC']
        self.insurance_attributes['car'] = self.car.pk
        serializer = InsuranceSerializer(instance=self.insurance, data=self.insurance_attributes)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors.keys()), set(['type_of_insurance']))

    def test_validate_way_of_purchase(self):
        self.insurance_attributes['car'] = self.car.pk
        self.insurance_attributes['type_of_insurance'] = ['AC', 'OC']
        serializer = InsuranceSerializer(instance=self.insurance, data=self.insurance_attributes)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors.keys()), {'non_field_errors'})

    def test_validate_date(self):
        self.insurance_attributes['car'] = self.car.pk
        self.insurance_attributes['end_date'] = datetime.date(2019, 3, 30)
        serializer = InsuranceSerializer(instance=self.insurance, data=self.insurance_attributes)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors.keys()), {'non_field_errors'})
