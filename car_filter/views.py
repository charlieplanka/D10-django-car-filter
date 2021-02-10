from django.shortcuts import render
from .models import Car
from django.views.generic import ListView
from django.db.models import Q


class CarListView(ListView):
    model = Car

    def get_queryset(self):
        qs = super().get_queryset()
        get_params = self.request.GET.dict()

        # filter
        filter_params = Q()
        for key, value in get_params.items():
            if value:
                filter_params.add(Q(**{key: value}), Q.AND)
        qs = qs.filter(filter_params)
        return qs
