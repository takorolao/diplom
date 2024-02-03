from django.apps import AppConfig

# Класс конфигурации приложения "Goods"
class GoodsConfig(AppConfig):
    # Указание типа автоматически создаваемого поля первичного ключа (BigAutoField)
    default_auto_field = 'django.db.models.BigAutoField'
    # Название приложения
    name = 'goods'
    # Человекочитаемое название приложения (отображается в админ-панели Django)
    verbose_name = 'Товары'
