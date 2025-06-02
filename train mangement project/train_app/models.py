from django.db import models

class Train(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    seats_available = models.IntegerField(default=100)
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.number}) - {self.source} to {self.destination}"