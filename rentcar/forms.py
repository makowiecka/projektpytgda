from django import forms
from django.forms import DateInput

from car.models import Car
from rentcar.models import UserCarRent


class RentCarForm(forms.ModelForm):
    rent_date = forms.DateField(
        label = 'Data wypożyczenia',
        widget=forms.SelectDateWidget
    )
    return_date = forms.DateField(
        label = 'Data zwrotu',
        widget=forms.SelectDateWidget
    )

    class Meta:
        model = UserCarRent
        fields = ('rent_date', 'return_date')
