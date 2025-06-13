from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'first_name', 'last_name', 'email',
            'address', 'phone', 'postal_code', 'city'
        ]
        # Добавим verbose_name для полей формы, если они не берутся из модели автоматически
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Email',
            'address': 'Адрес доставки',
            'phone': 'Телефон',
            'postal_code': 'Почтовый индекс',
            'city': 'Город',
        }


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