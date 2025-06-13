from django.db import models
from django.urls import reverse # Для метода get_absolute_url
from django.utils.text import slugify # Для автоматического создания слага

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=100, blank=True, null=True, verbose_name='Слаг') # Убрали unique=True временно

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # Эта функция пока может вызвать ошибку, так как мы еще не настроили URL.
        # Пока оставим ее, но имей в виду.
        return reverse('products:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория',
                                 null=True, blank=True) # null/blank True, чтобы можно было оставить без категории
    name = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=200, blank=True, null=True, verbose_name='Слаг')
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name='Изображение') # Добавили поле для изображения
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    stock = models.PositiveIntegerField(default=0, verbose_name='Количество на складе') # Добавили количество на складе
    available = models.BooleanField(default=True, verbose_name='Доступен') # Добавили флаг доступности
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления') # Добавили поле для даты обновления

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
        ]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # Эта функция пока может вызвать ошибку, так как мы еще не настроили URL.
        return reverse('products:product_detail', args=[self.id, self.slug])
