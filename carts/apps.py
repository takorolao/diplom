from django.apps import AppConfig

# Класс конфигурации приложения "Carts"
class CartsConfig(AppConfig):
    # Указание типа автоматически создаваемого поля первичного ключа (BigAutoField)
    default_auto_field = 'django.db.models.BigAutoField'
    # Название приложения
    name = 'carts'
    # Человекочитаемое название приложения (отображается в админ-панели Django)
    verbose_name = "Корзины"
