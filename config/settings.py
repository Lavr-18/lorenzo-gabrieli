import os
from dotenv import load_dotenv
from pathlib import Path
from django.contrib.messages import constants as messages # Импорт для MESSAGE_TAGS

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / '.env') # Загрузка переменных окружения из .env

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = os.getenv('DEBUG') == 'True' # DEBUG из .env

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(',') # ALLOWED_HOSTS из .env


# Application definition

INSTALLED_APPS = [
    # стандартные приложения Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # наши приложения
    'users',
    'products',
    'cart',
    'orders',
]

# Сообщения Django с классами Bootstrap (для красивого отображения)
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls' # Убедись, что это единственное объявление ROOT_URLCONF

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"], # Путь к общему каталогу шаблонов проекта
        'APP_DIRS': True, # Разрешает Django искать шаблоны в папках templates каждого приложения
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us' # Можно изменить на 'ru', если основной язык русский

TIME_ZONE = 'UTC' # Можно изменить на 'Europe/Moscow' или другую подходящую временную зону

USE_I18N = True # Включить поддержку интернационализации

USE_TZ = True # Включить поддержку часовых поясов (рекомендуется)


# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' # Тип первичного ключа по умолчанию

AUTH_USER_MODEL = 'users.CustomUser' # Указываем нашу кастомную модель пользователя

# URL-адреса для аутентификации
LOGIN_REDIRECT_URL = 'product_list' # Куда перенаправлять после успешного входа
LOGOUT_REDIRECT_URL = 'users:login' # Куда перенаправлять после выхода
LOGIN_URL = 'users:login' # URL для страницы входа (если пользователь не авторизован)


# Static files (CSS, JavaScript, Images) и Media files (загружаемые пользователем)
# https://docs.djangoproject.com/en/5.2/howto/static-files/
# https://docs.djangoproject.com/en/5.2/howto/static-files/serving-files-in-development/

STATIC_URL = '/static/' # URL для статических файлов

# Папки, в которых Django будет искать статические файлы (например, общие CSS, JS, изображения проекта)
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Путь, куда Django будет собирать статические файлы для продакшена (команда collectstatic)
STATIC_ROOT = BASE_DIR / 'staticfiles'

# MEDIA_URL и MEDIA_ROOT для загружаемых пользователями файлов (например, изображения товаров)
MEDIA_URL = '/media/' # URL для медиа-файлов
MEDIA_ROOT = BASE_DIR / 'media' # Путь на диске, где будут храниться медиа-файлы