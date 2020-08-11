import uuid

from PIL import Image
from django.db import models

# Create your models here.

class CarStatus(models.Model):
    car_status = models.TextField()

    def __str__(self):
        return self.car_status

    class Meta:
        verbose_name_plural = 'Car statuses'

class Car(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    brand = models.CharField(max_length=20, blank=False, null=False)
    model = models.CharField(max_length=20, blank=False, null=False)
    production_year = models.CharField(max_length=20, blank=False, null=False)
    image = models.ImageField(default='default.jpg', upload_to='cars_pics')
    status = models.ForeignKey(CarStatus, default=2, on_delete=models.PROTECT)

    def __str__(self):
        return self.brand

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 200 or img.width > 200:
            output_size=(200,200)
            img.thumbnail(output_size)
            img.save(self.image.path)

    class Meta:
        verbose_name_plural = 'Cars'

# class CarStatus(models.Model):
#     car_status = models.TextField()
#
#     def __str__(self):
#         return self.car_status
#
#     class Meta:
#         verbose_name_plural = 'Car statuses'
