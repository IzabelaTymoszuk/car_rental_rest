from rest_framework.test import APITestCase
from ...models.car import Car
import datetime


class CarModelTests(APITestCase):
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

    def test_str_method(self):
        car = self.car
        car_name = car.__str__()
        self.assertEqual(str(car), car_name)
