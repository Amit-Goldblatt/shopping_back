from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, CartItem
from product.serializers import ProductSerializer
from .serializers.ProductSerializer import ProductSerializer as P
from .serializers.CartSerializer import CartSerializer , CartSerializerFull
@api_view(['GET', 'POST'])
def product_list(request):
  
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = P(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = P(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = P(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = P(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.soft_delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def cart_list(request):
    if request.method == 'GET':
        cart = CartItem.objects.all()
        serializer = CartSerializerFull(cart, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def cart_detail(request, pk):
    try:
        cart = CartItem.objects.get(pk=pk)
    except CartItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cart.soft_delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

