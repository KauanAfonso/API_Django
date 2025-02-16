from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import PedidoSerializer
from .models import Pedido
# Create your views here.

@api_view(["GET"]) 
def get_pedido(request):
    return Response(PedidoSerializer({"nome_pedido": "oi", "descricao": "2341"}).data)


@api_view(["POST"]) 
def create_pedido(request):
   serializer = PedidoSerializer(data=request.data)
   if serializer.is_valid():
       serializer.save()
       return Response(serializer.data, status=status.HTTP_201_CREATED)
   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)