from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from ...models.rent import Rent
from ...models.car import Car
from ...serializers.rent import RentSerializer
import datetime

User = get_user_model()


class RentSerializerTests(APITestCase):
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
            'next_review_date': datetime.date(2019, 12, 30)
        }
        self.car = Car.objects.create(**self.car_attributes)

        self.car_attributes_status = {
            'status': 'Ch',
            'make': 'Citroen',
            'model': 'C4',
            'price_per_day': 30,
            'body_styles': 'C',
            'way_of_purchase': 'L',
            'fuel_types': ['P'],
            'color': 'Red',
            'engine': '1.4',
            'VIN': 'ASGH654KJK9835679',
            'transmission': 'M',
            'year_of_manufacture': 2017,
            'next_review_date': datetime.date(2019, 12, 30)
        }
        self.car_status = Car.objects.create(**self.car_attributes_status)

        self.superuser_attributes = {
            'username': 'admin',
            'email': 'admin@admin.com',
            'password': 'admin123456'
        }
        self.superuser = User.objects.create_superuser(**self.superuser_attributes)

        self.rent_attributes = {
            'start_rent': datetime.date(2019, 9, 6),
            'end_rent': datetime.date(2019, 9, 7),
            'deposit': 1000,
            'user': self.superuser,
            'car': self.car
        }

        self.rent = Rent.objects.create(**self.rent_attributes)
        self.rent_serializer = RentSerializer(instance=self.rent)


    def test_contains_expected_fields(self):
        data = self.rent_serializer.data
        self.assertEqual(set(data.keys()), set(['start_rent', 'end_rent', 'deposit', 'number_of_day', 'amount', 'car']))

    def test_validate_date_end_start(self):
        self.rent_attributes['start_rent'] = datetime.date(2019, 9, 8)
        self.rent_attributes['car'] = self.car.pk
        serializer = RentSerializer(instance=self.rent, data=self.rent_attributes)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors.keys()), {'non_field_errors'})

    def test_validate_date_end_today(self):
        self.rent_attributes['end_rent'] = datetime.date(2019, 8, 30)
        self.rent_attributes['car'] = self.car.pk
        serializer = RentSerializer(instance=self.rent, data=self.rent_attributes)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors.keys()), {'non_field_errors'})

    def test_validate_date_start_today(self):
        self.rent_attributes['start_rent'] = datetime.date(2019, 8, 30)
        self.rent_attributes['car'] = self.car.pk
        serializer = RentSerializer(instance=self.rent, data=self.rent_attributes)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors.keys()), {'non_field_errors'})

    def test_validate_car_status(self):
        self.rent_attributes['car'] = self.car_status.pk
        serializer = RentSerializer(instance=self.rent, data=self.rent_attributes)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors.keys()), {'non_field_errors'})
