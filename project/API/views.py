from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import PedidoSerializer
from .models import Pedido
# Create your views here.

@api_view(["GET"]) 
def get_pedido(request):
    return Response(PedidoSerializer({"nome_pedido": "oi", "descricao": "2341"}).data)
