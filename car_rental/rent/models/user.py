from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField



DRIVING_LICENSE_PERMISSION = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('E', 'E')
)


class RenterUser(AbstractUser):
    company = models.CharField(max_length=100, blank=True, null=True)
    driving_license_number = models.CharField(max_length=10, blank=True, null=True, unique=True)
    categories_of_vehicles = MultiSelectField(choices=DRIVING_LICENSE_PERMISSION, max_choices=5, max_length=1,
                                              blank=True, null=True)
    PESEL = models.IntegerField(blank=True, null=True, unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'