from django.db import models
from .car import Car
from multiselectfield import MultiSelectField

TYPE_INSURANCE = (
    ('AC', 'Autocasco'),
    ('OC', 'OC'),
    ('NWW', 'NWW')
)


class Insurance(models.Model):
    insurance_status = models.BooleanField(default=True)
    insurance_company = models.CharField(max_length=100)
    end_date = models.DateField()
    type_of_insurance = MultiSelectField(choices=TYPE_INSURANCE, max_choices=3, max_length=10)
    worth_of_insurance = models.DecimalField(max_digits=8, decimal_places=2)
    car = models.ForeignKey(Car, on_delete=models.PROTECT, related_name='car_insurance')
    insurance_number = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.insurance_company} {self.insurance_number} - {self.car}'

    class Meta:
        ordering = ['end_date']

