from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from ...models.rent import Rent
from ...models.car import Car
import datetime

User = get_user_model()


class RentModelTests(APITestCase):
    def setUp(self):
        self.car = Car.objects.create(
            status='A',
            make='Citroen',
            model='C4',
            price_per_day=30,
            body_styles='C',
            way_of_purchase='FM',
            fuel_types='P',
            color='Red',
            engine='1.4',
            VIN='ASGH654HJK9835679',
            transmission='M',
            year_of_manufacture=2016,
            next_review_date=datetime.datetime.strptime('2020-03-02', '%Y-%m-%d')
        )
        self.superuser = User.objects.create_superuser(
            'admin',
            'admin@admin.com',
            'admin123456'
        )
        self.rent = Rent.objects.create(
            start_rent=datetime.datetime.strptime('2019-08-28', '%Y-%m-%d'),
            end_rent=datetime.datetime.strptime('2019-08-29', '%Y-%m-%d'),
            deposit=1000,
            user=self.superuser,
            car=self.car
        )

    def test_str_method(self):
        rent = self.rent
        rent_name = rent.__str__()
        self.assertEqual(str(rent), rent_name)

    def test_number_of_day(self):
        self.assertEqual(self.rent.number_of_day, 1)

    def test_amout(self):
        self.assertEqual(self.rent.amount, 30)
