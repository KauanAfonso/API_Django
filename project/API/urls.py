from django.urls import path
from .views import get_pedido

urlpatterns = [
    path('pedidos/', get_pedido, name='get_pedido')
]

