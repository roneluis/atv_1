from django.shortcuts import render
from . models import Product
from . forms import ProductForm

def home (request):
    return render(request, 'home.html')

def product_list (request):
    products = Product.objects.all()
    return render(request, 'list.html/', {'products':products})
   
def name_order (request):
    products=Product.objects.order_by('name')
    return render(request, 'list.html/', {'products':products})

def lowest_price (request):
    products=Product.objects.order_by('price')
    return render(request, 'list.html/', {'products':products})

def bigger_price (request):
    products=Product.objects.order_by('-price')
    return render(request, 'list.html/', {'products':products})
# Create your views here.
