from django.contrib import admin

# Register your models here.
from car.models import Car, CarStatus
from . import models

class CarAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(models.Car, CarAdmin)
admin.site.register(models.CarStatus)
