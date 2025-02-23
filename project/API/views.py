from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import orderserializer
from .models import Order
# Create your views here.

#obtendo todos os pedidos
@api_view(["GET"])
def get_orders(request):
    orders = Order.objects.all()#pegando todos os objetos
    serializer = orderserializer(orders, many=True) #serializando todos 
    return Response(serializer.data) #retornando


#uuilizando os outros metodos por id
@api_view(["GET" , "DELETE", "PUT"]) 
def Order_detail(request, pk):
    try:
        id_Order = Order.objects.get(pk=pk) #pegando somente o que tem id
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) #se não existir
    
    if request.method == "GET":
        serializer = orderserializer(id_Order)
        return Response(serializer.data)
    
    if request.method == "DELETE":
        operacao = id_Order.delete()
        if operacao:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "PUT":
        serializer = orderserializer(id_Order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#criando com post
@api_view(["POST"]) 
def create_Order(request):
   serializer = orderserializer(data=request.data)
   if serializer.is_valid():
       serializer.save()
       return Response(serializer.data, status=status.HTTP_201_CREATED)
   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#fim

