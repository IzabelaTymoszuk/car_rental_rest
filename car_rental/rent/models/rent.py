from django.db import models
from .car import Car
from .user import RenterUser


class Rent(models.Model):
    start_rent = models.DateField()
    end_rent = models.DateField()
    deposit = models.DecimalField(max_digits=7, decimal_places=2)
    user = models.ForeignKey(RenterUser, related_name='renter', on_delete=models.SET_NULL, null=True)
    car = models.ForeignKey(Car, on_delete=models.PROTECT, related_name='rent')

    @property
    def number_of_day(self):
        delta = self.end_rent - self.start_rent
        return delta.days

    @property
    def amount(self):
        return self.car.price_per_day * self.number_of_day

    def __str__(self):
        return f'{self.car} rent for {self.number_of_day} days'
