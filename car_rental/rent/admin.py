from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.


from .models.car import Car
from .models.insurance import Insurance
from .models.rent import Rent
from .models.user import RenterUser

admin.site.register(Car)
admin.site.register(Insurance)
admin.site.register(Rent)
admin.site.register(RenterUser, UserAdmin)