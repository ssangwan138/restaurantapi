from rest_framework import serializers
from menu.models import MenuItem

from menu.serializers import MenuItemSerializer
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    menuitems = MenuItemSerializer(
         many=True
    )
    class Meta:
        model = Order
        fields = '__all__'
