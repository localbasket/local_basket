from django.db import models

from django.contrib.auth.models import User # Don't need this time

# Create your models here.

class Pin(models.Model):
    pin=models.IntegerField()

    def __int__(self):
        return self.pin

class Location(models.Model):
    location_name=models.CharField(max_length=200)
    pin=models.ForeignKey(to=Pin,on_delete=models.CASCADE) # on_delete=models.CASCADE

    def __str__(self):
        return self.location_name
