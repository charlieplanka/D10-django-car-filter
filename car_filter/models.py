from django.db import models


class Car(models.Model):
    TRANSMISSION_CHOICES = [
        (1, "механика"),
        (2, "автомат"),
        (3, "робот"),
    ]

    manufacturer = models.CharField(max_length=200)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    transmission = models.SmallIntegerField(choices=TRANSMISSION_CHOICES)
    color = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.manufacturer} {self.model}"

