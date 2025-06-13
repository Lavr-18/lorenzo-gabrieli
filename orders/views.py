# lorenzo-gabrieli/orders/views.py
from django.shortcuts import render, redirect
from .models import OrderItem, Order # Убедись, что Order тоже импортирован
from .forms import OrderCreateForm
from products.models import Product
from django.contrib.auth.decorators import login_required # Добавим для потенциального использования


def order_create(request):
    cart = request.session.get('cart', {})
    if not cart:
        # Если корзина пуста, перенаправляем на страницу корзины с сообщением
        # (можно добавить messages.info, если настроены)
        return redirect('cart:cart_detail') # Используем 'cart:cart_detail' с неймспейсом

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            # НЕ СОХРАНЯЕМ СРАЗУ, чтобы сначала присвоить пользователя
            order = form.save(commit=False)

            # Если пользователь авторизован, привязываем его к заказу
            if request.user.is_authenticated:
                order.user = request.user
                # Можно также заполнить email, first_name, last_name и phone
                # из данных пользователя, чтобы избежать дублирования ввода.
                # Но пока оставим, чтобы форма гостевого заказа работала.
                if not order.first_name and request.user.first_name:
                    order.first_name = request.user.first_name
                if not order.last_name and request.user.last_name:
                    order.last_name = request.user.last_name
                if not order.email and request.user.email:
                    order.email = request.user.email
                if not order.phone and hasattr(request.user, 'phone') and request.user.phone:
                    order.phone = request.user.phone


            order.save() # Теперь сохраняем объект заказа в базе данных

            # Создаем элементы заказа
            for product_id_str, quantity in cart.items():
                product_id = int(product_id_str) # Важно преобразовать ключ в int
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
        # Если пользователь авторизован, предзаполняем форму его данными
        initial_data = {}
        if request.user.is_authenticated:
            initial_data['first_name'] = request.user.first_name
            initial_data['last_name'] = request.user.last_name
            initial_data['email'] = request.user.email
            # Проверяем наличие поля 'phone' у CustomUser, прежде чем пытаться получить его
            if hasattr(request.user, 'phone'):
                initial_data['phone'] = request.user.phone
            # Если у тебя есть поля адреса в CustomUser, можно их тоже предзаполнить
            # initial_data['address'] = request.user.address
            # initial_data['postal_code'] = request.user.postal_code
            # initial_data['city'] = request.user.city

        form = OrderCreateForm(initial=initial_data)
    return render(request, 'orders/order_create.html', {'form': form})