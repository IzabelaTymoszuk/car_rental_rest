from rest_framework.test import APITestCase
from ...models.insurance import Insurance
from ...models.car import Car
import datetime


class InsuranceModelTests(APITestCase):
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
        self.insurance = Insurance.objects.create(
            insurance_status=True,
            insurance_company='AXA',
            end_date=datetime.date(2019, 12, 9),
            type_of_insurance='OC',
            worth_of_insurance=300000,
            car=self.car,
            insurance_number='JHVS675/76576/19'
        )

    def test_str_method(self):
        insurance = self.insurance
        insurance_name = insurance.__str__()
        self.assertEqual(str(insurance), insurance_name)
