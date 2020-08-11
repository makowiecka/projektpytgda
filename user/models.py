from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    card_number = models.CharField(
        verbose_name="Numer karty użytkownika",
        max_length=6, null=False, blank=False
    )

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.card_number:
            card_number = User.objects.count() + 1
            self.card_number=str(card_number).zfill(6)

        return super(User, self).save(*args, **kwargs)