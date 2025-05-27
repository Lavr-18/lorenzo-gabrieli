# Lorenzo Gabrieli — Интернет-магазин на Django

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Django](https://img.shields.io/badge/Django-4.x-success)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Made with](https://img.shields.io/badge/Made%20with-%F0%9F%96%A5%EF%B8%8F%20Django-blue)


Это веб-приложение интернет-магазина одежды, разработанное на Django. Включает каталог товаров, категории, корзину и административную панель.

## 📦 Возможности

- Просмотр списка товаров
- Фильтрация по категориям
- Страница с деталями товара
- Добавление/удаление товаров в корзину
- Корзина хранится в сессии
- Админ-панель для управления товарами и категориями

## 🚀 Технологии

- Python 3.10+
- Django 4.x
- HTML + Django Templates
- SQLite (по умолчанию)
- Bootstrap (опционально)

## 🔧 Установка

1. Клонируй репозиторий:

```bash
git clone https://github.com/ИМЯ_ПОЛЬЗОВАТЕЛЯ/lorenzo_gabrieli.git
cd lorenzo_gabrieli
```

Создай виртуальное окружение и активируй его:

```bash
python -m venv venv
source venv/bin/activate  # для Linux/macOS
venv\Scripts\activate     # для Windows
```

Установи зависимости:
```bash
pip install -r requirements.txt
```

Примени миграции:
```
bash
python manage.py migrate
```

Создай суперпользователя:
```
bash
python manage.py createsuperuser
```

Запусти сервер:
```bash
python manage.py runserver
```


Перейди на http://127.0.0.1:8000/ — и ты в магазине!

lorenzo_gabrieli/
├── cart/                 # корзина
├── products/             # товары и категории
├── templates/            # шаблоны
├── static/               # статические файлы
├── manage.py
└── ...

🛠️ План разработки
 Категории и товары

 Детальная страница товара

 Корзина на сессиях

 Оформление заказа

 Подключение платежей
