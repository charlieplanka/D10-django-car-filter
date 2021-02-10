from django.shortcuts import render
from .models import Car
from django.views.generic import ListView
from django.db.models import Q


class CarListView(ListView):
    model = Car

    def get_queryset(self):        
        # filter
        get_params = self.request.GET.dict()
        filter_params = Q()
        for key, value in get_params.items():
            if value:
                filter_params.add(Q(**{f'{key}__icontains': value.strip()}), Q.AND)
        return Car.objects.filter(filter_params)
