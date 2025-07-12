from django.db import models
from datetime import datetime

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    add_date = models.CharField(max_length=50, null=True)
    exp_date = models.CharField(max_length=50, null=True)
    date_time = models.DateTimeField(auto_now_add =True, null=True)

    def __str__(self):
        return self.name