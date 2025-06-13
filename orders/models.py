from django.db import models
from products.models import Product
from django.contrib.auth import get_user_model # Импортируем get_user_model


User = get_user_model() # Получаем твою кастомную модель пользователя CustomUser

class Order(models.Model):
    # Ссылка на пользователя. null=True, blank=True позволяет гостевые заказы.
    user = models.ForeignKey(User,
                             on_delete=models.SET_NULL, # При удалении пользователя, заказ не удаляется, а user становится NULL
                             related_name='orders', # Обратная связь от User к Order
                             null=True,
                             blank=True,
                             verbose_name='Пользователь')

    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Email')
    address = models.CharField(max_length=250, verbose_name='Адрес доставки')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False, verbose_name='Оплачен')

    # Добавлено
    postal_code = models.CharField(max_length=20, blank=True, null=True, verbose_name='Почтовый индекс') # Добавил verbose_name
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name='Город') # Добавил verbose_name

    class Meta:
        ordering = ['-created']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ №{self.id}'

    # Метод для получения общей стоимости заказа
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена на момент покупки')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    class Meta:
        verbose_name = 'Позиция заказа' # Добавил verbose_name
        verbose_name_plural = 'Позиции заказа' # Добавил verbose_name_plural

    def __str__(self):
        return f'{self.product.name} (x{self.quantity})'

    def get_cost(self):
        return self.price * self.quantity

