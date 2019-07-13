from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products' : products} )