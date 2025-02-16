from django.urls import path
from .views import get_pedido, create_pedido

urlpatterns = [
    path('pedidos/', get_pedido, name='get_pedido'),
    path('pedidos/create', create_pedido, name='create_pedido')
]

