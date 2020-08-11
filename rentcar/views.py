from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from car.models import Car, CarStatus
from rentcar.forms import RentCarForm
from rentcar.models import UserCarRent


class RentCarView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = 'login'
    template_name = 'rentcar/rent.html'
    model = UserCarRent
    form_class = RentCarForm
    success_message = 'Samochód został wypożyczony'


    def form_valid(self, form):
        car = get_object_or_404(Car, pk=self.kwargs.get("pk"))
        form.instance.car = car
        car.status = CarStatus(1)
        form.instance.user = self.request.user
        car.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')
