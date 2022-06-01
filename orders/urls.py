from django.urls import path
from .views import createOrder, prevOrders, orderStatus

urlpatterns = [
    path('createOrder/', createOrder.as_view()),
    path('prevOrders/', prevOrders.as_view()),
    path('orderStatus/<int:id>', orderStatus.as_view()),
 ] 
# Create order.
# - View order status
# - View past orders