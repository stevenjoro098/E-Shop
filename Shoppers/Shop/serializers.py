from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ("name","slug","image","price",)
        model = Product
