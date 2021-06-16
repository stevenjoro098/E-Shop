from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from rest_framework.decorators import api_view
import random
from .models import Product, Category
from .serializers import ProductSerializer
from rest_framework import generics
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.request import Request


# Create your views here.

class ProductApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductList(ListView):
    model = Product
    template_name = 'Shop/product_list.html'


class ProductDetail(DetailView):
    template_name = 'Shop/product_detail.html'

    model = Product


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
    products = products.filter(category=category)
    return render(request,
                  'shop/product_list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)

    return render(request, 'Shop/product_detail.html', {'product': product})


def generate_random_string(length):
    sample_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'
    results = ''.join((random.choice(sample_characters) for i in range(length)))
    print("random string is:", results)
    return results


@csrf_exempt
@api_view(['POST'])
def reference_code(request):
    if request.method == 'POST':
        data = Request.DATA
        # print(data.json())

    return HttpResponse(generate_random_string(5))
