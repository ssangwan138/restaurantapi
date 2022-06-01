from django.db import models
from menu.models import MenuItem
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    total_price = models.FloatField(default=0)
    menuitems = models.ManyToManyField(MenuItem, blank=True)
    PLACED = 'pending'
    PREPARING = 'preparing'
    READY = 'ready'
    ORDER_STATUS_CHOICES = [
        (PLACED, "placed"),
        (PREPARING, "preparing"),
        (READY, "ready"),
    ]
    status = models.CharField(
         choices=ORDER_STATUS_CHOICES,
         max_length=10,
         null=True
    )
    # status = models.CharField(default = "", max_length=30)

    def __str__(self):
        return str(self.id)