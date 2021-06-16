from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from Shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
@require_POST
def cart_add(request, pk):
    print('this is the pk value', pk)
    cart = Cart(request)
    print('initial crt', cart)
    product = get_object_or_404(Product, id=pk)
    print('the product id', product)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
        #print('the cart', cart)
    return redirect('cart:cart_detail')

def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('Shop:productlist')
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')
def cart_detail(request):
    cart = Cart(request)
    print(cart)
    return render(request, 'cart/detail.html', {'cart': cart})