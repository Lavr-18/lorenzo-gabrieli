from django.db import models
from products.models import Product
from django import forms


class Order(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Email')
    address = models.CharField(max_length=250, verbose_name='Адрес доставки')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False, verbose_name='Оплачен')

    # Добавлено
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ №{self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена на момент покупки')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    def __str__(self):
        return f'{self.product.name} (x{self.quantity})'

    def get_cost(self):
        return self.price * self.quantity



class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'first_name', 'last_name', 'email',
            'address', 'phone', 'postal_code', 'city'
        ]

    def clean_postal_code(self):
        data = self.cleaned_data.get('postal_code')
        if not data:
            raise forms.ValidationError("Введите почтовый индекс")
        return data

    def clean_city(self):
        data = self.cleaned_data.get('city')
        if not data:
            raise forms.ValidationError("Введите город")
        return data

