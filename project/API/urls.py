from django.urls import path
from .views import get_pedidos, create_pedido, pedido_detail

urlpatterns = [
    path('pedidos/', get_pedidos, name='get_pedidos'),
    path('pedidos/create', create_pedido, name='create_pedido'),
    path('pedidos/<int:pk>', pedido_detail, name='pedido_detail'),
]

