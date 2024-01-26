from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class services(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to="images/")
    description = models.TextField()
    def __str__(self):
        return self.name


class stylist(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name


class Bookings(models.Model):
    User = models.ForeignKey(
        "auth.User", null=True, blank=True, on_delete=models.CASCADE
    )
    date = models.DateField()
    time = models.TimeField()
    service = models.CharField(max_length=100)

    def __str__(self):
        return self.service
