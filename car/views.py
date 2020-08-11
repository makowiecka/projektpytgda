from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView, DetailView

from car.models import Car
from .filters import CarFilter

class CarListView(ListView):
    # login_url = '/login'
    template_name = "car/home.html"
    model = Car
    paginate_by = 2
    filterset_class = CarFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['filterset'] = self.filterset
        return context
    # def get_queryset(self):
    #     qs = self.model.objects.all()
    #     product_filter_list = CarFilter(self.request.GET, queryset=qs)
    #     return product_filter_list.qs
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filter'] = CarFilter(self.request.GET, queryset=self.get_queryset())
    #     return context

class CarDetailView(DetailView):
    template_name = "car/car_detail.html"
    model = Car
    # queryset = Car.objects.all()

    # def get_object(self, queryset=None):
    #     id_ = self.kwargs.get("id")
    #     return get_object_or_404(Car, id=id_)

