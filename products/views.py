from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})


def detail(request, product_id):
    product_dtl = Product.objects.get(pk=product_id)
    return render(request, 'products/product_detail.html', {'product_dtl': product_dtl})
