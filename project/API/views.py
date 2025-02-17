from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import orderserializer
from .models import Order
# Create your views here.


@api_view(["GET"])
def get_orders(request):
    orders = Order.objects.all()
    serializer = orderserializer(orders, many=True)
    return Response(serializer.data)

@api_view(["GET" , "DELETE", "PUT"]) 
def Order_detail(request, pk):
    try:
        id_Order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
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


@api_view(["POST"]) 
def create_Order(request):
   serializer = orderserializer(data=request.data)
   if serializer.is_valid():
       serializer.save()
       return Response(serializer.data, status=status.HTTP_201_CREATED)
   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



