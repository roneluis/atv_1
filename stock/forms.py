from django.urls import path
from . models import Product

class ProductForm():
    class Meta:
        model = Product
        fields= '__all__'