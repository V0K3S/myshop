from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm

@require_POST
def cart_add(request, product_id):
    cart = cart(request)
    product = get_object_or_404(product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_details(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})

def product_detail(request, id, slug):
    product = get_object_or_404(product, id=id, slug=slug, available=True)
    
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/details.html', {
        'product': product,
        'cart_product_form': cart_product_form})