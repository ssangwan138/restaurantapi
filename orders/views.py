from django.shortcuts import render
from .models import Order, MenuItem
from .serializers import  OrderSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
class createOrder(APIView):
    def post(self, request, format=None):
        order = Order.objects.create()
        total=0
        for i in request.data.get('pid'):
            p=MenuItem.objects.get(id = i)
            total=total+p.price
            order.menuitems.add(p)
        order.total_price=total
        order.status = "Accepted"
        order.save()
        print(order.menuitems)
        return Response({'success' : 'New Order Created'})

class prevOrders(APIView):
    def get(self, request):
        order = Order.objects.all()
        print(order)

        serializer = OrderSerializer(order,many=True)
        return Response(serializer.data)