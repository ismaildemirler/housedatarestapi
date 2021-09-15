from django.db import models
from .managers import HouseManager
from django.contrib.postgres.fields import ArrayField

class HousesData(models.Model):
    house_id = models.UUIDField()
    price = models.IntegerField()
    transaction_date = models.DateField()
    post_code = models.CharField(max_length=50)
    home_type = models.CharField(max_length=1)
    unknown1 = models.CharField(max_length=1)
    unknown2 = models.CharField(max_length=1)
    paon = models.CharField(max_length=150)
    saon = models.CharField(max_length=150)
    street = models.CharField(max_length=150)
    locality = models.CharField(max_length=150)
    town = models.CharField(max_length=150)
    district = models.CharField(max_length=150)
    county = models.CharField(max_length=150)
    unknown3 = models.CharField(max_length=1)
    unknown4 = models.CharField(max_length=1)

    objects = HouseManager()


class AverageHousePrice(models.Model):
    average_price = models.FloatField()
    transaction_date = models.DateField()
    year_month = models.CharField(max_length=10)
    year = models.IntegerField()
    month = models.IntegerField()
    post_code = models.CharField(max_length=10)
    home_type = models.CharField(max_length=1)



class NumberOfTransactions(models.Model):
    price_range = ArrayField(ArrayField(models.IntegerField()))
    transaction_count = models.IntegerField()