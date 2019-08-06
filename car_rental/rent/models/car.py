from django.db import models
from multiselectfield import MultiSelectField
from datetime import date


STATUS_CAR = (
    ('Ch', 'Checked'),
    ('A', 'Available'),
    ('InR', 'In_Repair'),
    ('R', 'Rental'),
    ('F', 'In_the_future'),
    ('Un', 'Unavailable')
)

BODY_STYLES_CAR = (
    ('Se', 'Sedan'),
    ('V', 'Van'),
    ('C', 'Coupe'),
    ('H', 'Hatchback'),
    ('M', 'Minivan'),
    ('S', 'SUV')
)

WAY_PURCHASE = (
    ('L', 'Leasing'),
    ('FM', 'For_Money')
)

FUEL = (
    ('D', 'Diesel'),
    ('P', 'Petrol'),
    ('E', 'Electric'),
    ('G', 'Gasoline'),
    ('H', 'Hybrid')
)

TRANSMISSION_CAR = (
    ('AM', 'Automanual'),
    ('A', 'Automatic'),
    ('M', 'Manual')
)


class Car(models.Model):
    status = models.CharField(max_length=3, choices=STATUS_CAR)
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=40)
    price_per_day = models.DecimalField(max_digits=6, decimal_places=2)
    body_styles = models.CharField(max_length=2, choices=BODY_STYLES_CAR)
    way_of_purchase = models.CharField(max_length=2, choices=WAY_PURCHASE)
    fuel_types = MultiSelectField(choices=FUEL, max_choices=3, max_length=3)
    color = models.CharField(max_length=20)
    engine = models.CharField(max_length=40)
    VIN = models.CharField(max_length=17, unique=True)
    transmission = models.CharField(max_length=2, choices=TRANSMISSION_CAR)
    year_of_manufacture = models.IntegerField()
    next_review_date = models.DateField(default=date.today)

    def __str__(self):
        return f'{self.make} {self.model} {self.engine} {self.year_of_manufacture}'

    class Meta:
        ordering = ['make', 'model']