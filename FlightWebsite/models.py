from django.db import models

#Create your views here
class Flight(models.Model):
    flight_number = models.CharField(max_length=50)
    departure_city = models.CharField(max_length=100)
    arrival_city = models.CharField(max_length=100)
    departure_date = models.DateField()
    arrival_date = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    seats_available = models.IntegerField()

    def __str__(self):
        return self.flight_number
