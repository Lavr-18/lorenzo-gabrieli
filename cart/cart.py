class Cart:
    def __init__(self, request):
        """
        Инициализация корзины с привязкой к сессии пользователя.
        """
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            # если корзины нет в сессии, создаём пустую
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """
        Добавить товар в корзину или обновить количество.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price),
            }
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Помечаем сессию как изменённую, чтобы Django сохранил изменения
        self.session.modified = True

    def remove(self, product):
        """
        Удалить товар из корзины.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        # Очистить корзину
        self.session['cart'] = {}
        self.save()

    def __iter__(self):
        """
        Итератор по товарам корзины с добавлением объекта Product.
        """
        product_ids = self.cart.keys()
        from products.models import Product
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart_item = cart[str(product.id)]
            cart_item['product'] = product
            cart_item['total_price'] = float(cart_item['price']) * cart_item['quantity']
            yield cart_item

    def __len__(self):
        """
        Подсчитать общее количество товаров в корзине.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        Подсчитать общую стоимость корзины.
        """
        return sum(float(item['price']) * item['quantity'] for item in self.cart.values())
