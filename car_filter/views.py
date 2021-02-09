from django.shortcuts import render
from .models import Car
from django.views.generic import ListView


class CarListView(ListView):
    model = Car
