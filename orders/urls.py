from django.urls import path
from .views import createOrder, prevOrders

urlpatterns = [
    path('createOrder/', createOrder.as_view()),
    path('prevOrders/', prevOrders.as_view()),
    # path('order/prevOrders/', searchMenu.as_view()),
 ] 
# Create order.
# - View order status
# - View past orders