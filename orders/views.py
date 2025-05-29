from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm
from products.models import Product

def order_create(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('cart_detail')

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for product_id, quantity in cart.items():
                product = Product.objects.get(id=product_id)
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    price=product.price,
                    quantity=quantity
                )
            request.session['cart'] = {}  # очистить корзину
            return render(request, 'orders/order_created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order_create.html', {'form': form})
