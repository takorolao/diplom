from django.contrib import admin
from carts.models import Cart

# Создаем встроенный административный интерфейс для отображения корзин внутри админ-панели Django
class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = "product", "quantity", "created_timestamp"
    search_fields = "product", "quantity", "created_timestamp"
    readonly_fields = ("created_timestamp",)
    extra = 1

# Регистрируем встроенный интерфейс в админ-панели
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    # Определяем, какие поля отображать в списке объектов в админ-панели
    list_display = ["user_display", "product_display", "quantity", "created_timestamp",]
    # Добавляем фильтры для удобства поиска
    list_filter = ["created_timestamp", "user", "product__name",]

    # Определяем метод для отображения пользователя в списке объектов
    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        return "Анонимный пользователь"

    # Определяем метод для отображения продукта в списке объектов
    def product_display(self, obj):
        return str(obj.product.name)
