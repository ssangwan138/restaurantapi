from math import prod
from .models import  MenuItem
from rest_framework import generics, permissions, serializers, status
from .serializers import  MenuItemSerializer
from rest_framework.response import Response
from django.http import Http404

class viewMenu(generics.ListAPIView):
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()



class searchMenu(generics.ListAPIView):
    serializer_class = MenuItemSerializer
    def get_queryset(self):
        name = self.kwargs['name']
        menuItems = MenuItem.objects.filter(name__contains=name)
        return menuItems



class addMenuItem(generics.GenericAPIView):
    serializer_class = MenuItemSerializer

    def post(self, request, *args, **kwargs):
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
