from django.db import models
from datetime import datetime

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    userid = models.BigIntegerField()
    quantity = models.IntegerField()
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    isInMarketPlaces = models.BooleanField(null=True)
    description = models.TextField(max_length=1000, null=True)
    image = models.ImageField(upload_to='item_images/', null=True, blank=True)
    ItemCondition = models.IntegerField(null=True)
    isExpired = models.BooleanField(default=False)
    isAvailable = models.BooleanField(default=True)
    isSold = models.BooleanField(default=False)
    add_date = models.CharField(max_length=50, null=True)
    exp_date = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name
