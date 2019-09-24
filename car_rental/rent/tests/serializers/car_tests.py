from rest_framework.test import APITestCase
from ...models.car import Car
from ...serializers.car import CarSerializer
import datetime


class CarSerializerTests(APITestCase):
    def setUp(self):
        self.car_attributes = {
            'status': 'A',
            'make': 'Citroen',
            'model': 'C4',
            'price_per_day': 30,
            'body_styles': 'C',
            'way_of_purchase': 'FM',
            'fuel_types': ['P'],
            'color': 'Red',
            'engine': '1.4',
            'VIN': 'ASGH654HJK9835679',
            'transmission': 'M',
            'year_of_manufacture': 2016,
            'next_review_date': datetime.date(2020, 3, 2)
        }

        self.serializer_data = {
            'status': 'F',
            'make': 'Citroen',
            'model': 'C1',
            'price_per_day': 40,
            'body_styles': 'C',
            'way_of_purchase': 'FM',
            'fuel_types': ['P'],
            'color': 'Black',
            'engine': '1.4',
            'VIN': 'ASGH654HJK9835679',
            'transmission': 'M',
            'year_of_manufacture': 2019,
            'next_review_date': datetime.date(2020, 3, 2)
        }

        self.car = Car.objects.create(**self.car_attributes)
        self.car_serializer = CarSerializer(instance=self.car)

    def test_contains_expected_fields(self):
        data = self.car_serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'status', 'make', 'model', 'price_per_day', 'body_styles',
                                                'way_of_purchase', 'fuel_types', 'color', 'engine', 'VIN',
                                                'transmission', 'year_of_manufacture']))

    def test_status_field_content(self):
        data = self.car_serializer.data
        self.assertEqual(data['status'], self.car_attributes['status'])

    def test_validate_year_of_manufacture(self):
        self.car_attributes['year_of_manufacture'] = 1894
        serializer = CarSerializer(instance=self.car, data=self.car_attributes)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors.keys()), set(['year_of_manufacture']))

    def test_validate_VIN(self):
        self.car_attributes['VIN'] = 'ASGH654HJK98356898'
        serializer = CarSerializer(instance=self.car, data=self.car_attributes)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors.keys()), set(['VIN']))

    def test_validate(self):
        self.car_attributes['year_of_manufacture'] = 2020  # datetime.today().year +1
        self.car_attributes['status'] = 'A'
        serializer = CarSerializer(instance=self.car, data=self.car_attributes)
        self.assertFalse(serializer.is_valid())
        # import pdb; pdb.set_trace()
        self.assertEqual(set(serializer.errors.keys()), {'non_field_errors'})
