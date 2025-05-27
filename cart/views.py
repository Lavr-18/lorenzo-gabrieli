from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product


def cart_detail(request):
    cart = request.session.get('cart', {})
    products = []
    total_price = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        product.quantity = quantity
        product.total_price = product.price * quantity
        total_price += product.total_price
        products.append(product)

    context = {
        'products': products,
        'total_price': total_price,
    }
    return render(request, 'cart/cart_detail.html', context)


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    quantity = cart.get(str(product_id), 0)
    cart[str(product_id)] = quantity + 1  # увеличиваем количество на 1
    request.session['cart'] = cart
    return redirect('cart_detail')


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return redirect('cart_detail')
