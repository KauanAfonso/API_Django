from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import PedidoSerializer
from .models import Pedido
# Create your views here.


@api_view(["GET"])
def get_pedidos(request):
    pedidos = Pedido.objects.all()
    serializer = PedidoSerializer(pedidos, many=True)
    return Response(serializer.data)

@api_view(["GET" , "DELETE", "PUT"]) 
def pedido_detail(request, pk):
    try:
        id_pedido = Pedido.objects.get(pk=pk)
    except Pedido.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = PedidoSerializer(id_pedido)
        return Response(serializer.data)
    
    if request.method == "DELETE":
        operacao = id_pedido.delete()
        if operacao:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "PUT":
        serializer = PedidoSerializer(id_pedido, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"]) 
def create_pedido(request):
   serializer = PedidoSerializer(data=request.data)
   if serializer.is_valid():
       serializer.save()
       return Response(serializer.data, status=status.HTTP_201_CREATED)
   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



