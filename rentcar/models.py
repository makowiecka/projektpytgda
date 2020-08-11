import uuid

from django.db import models
from datetime import date

# Create your models here.
from car.models import Car
from user.models import User


class UserCarRent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    rent_date = models.DateField(default=date.today)
    return_date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.rent_date
