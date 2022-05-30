from django.db import models
from menu.models import MenuItem

# Create your models here.
class Order(models.Model):
    total_price = models.FloatField(default=0)
    menuitems = models.ManyToManyField(MenuItem, blank=True)
    status = models.CharField(default = "", max_length=30)

    def __str__(self):
        return str(self.id)