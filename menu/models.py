from django.db import models

# Create your models here.

class MenuItem(models.Model):
    name = models.CharField(max_length=15)
    image = models.ImageField(upload_to = 'images/')
    category = models.CharField(max_length=15, default="")
    price = models.IntegerField(default=0)
    discount = models.IntegerField(default = 0)
    plateSize = models.IntegerField(default = 0)

    def __str__(self):
        return self.name