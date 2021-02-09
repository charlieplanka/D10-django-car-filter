from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    @staticmethod
    def car(self):
        return self

    list_display = ('car', 'year', 'transmission', 'color')
