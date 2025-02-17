from django.urls import path
from .views import get_orders, create_Order, Order_detail

urlpatterns = [
    path('orders/', get_orders, name='get_orders'),
    path('orders/create', create_Order, name='create_Order'),
    path('orders/<int:pk>', Order_detail, name='Order_detail'),
]

O