from rest_framework import serializers
from product.models import CartItem
from .ProductSerializer import ProductSerializer


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'
    

class CartSerializerFull(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = CartItem
        fields = '__all__'
    