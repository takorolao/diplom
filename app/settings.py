# Импорт необходимых модулей
from pathlib import Path
from django.http import HttpResponseNotFound

# Определение базового каталога проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Секретный ключ для Django-приложения (хранится в тайне в продакшене)
SECRET_KEY = 'django-insecure-ld)8k$gfoow^#9-6mm@palg6l9d)&l!5ng#m2@=msxhq353g#2'

# Включение или отключение режима отладки
DEBUG = True

# Определение разрешенных хостов для приложения
ALLOWED_HOSTS = ['*']

# Список установленных приложений в проекте Django
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',

    "debug_toolbar",

    'main',
    'goods',
    'users',
    'carts',
    'orders',
]

# Промежуточные компоненты для обработки запросов и ответов
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

# Корневая конфигурация URL для проекта
ROOT_URLCONF = 'app.urls'

# Конфигурация шаблонов для проекта
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI-приложение для запуска проекта
WSGI_APPLICATION = 'app.wsgi.application'

# Конфигурация базы данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'home',
        'USER': 'home',
        'PASSWORD': 'home',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Конфигурация проверки пароля
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

# Настройки интернационализации
LANGUAGE_CODE = 'ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Конфигурация статических файлов (CSS, JavaScript, изображения)
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Настройки панели отладки
INTERNAL_IPS = [
    "127.0.0.1",
]

# Тип поля по умолчанию для первичного ключа
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Пользовательская модель пользователя и URL входа
AUTH_USER_MODEL = 'users.User'
LOGIN_URL = '/user/login/'
