from django.contrib import admin
from goods.models import Categories, Products

# Регистрация моделей в административной панели Django
# admin.site.register(Categories)
# admin.site.register(Products)

# Использование декоратора @admin.register для регистрации модели Categories
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    # Автоматическое заполнение поля slug на основе значения поля name
    prepopulated_fields = {"slug": ("name",)}
    # Отображаемые поля в списке объектов
    list_display = ["name",]

# Использование декоратора @admin.register для регистрации модели Products
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    # Автоматическое заполнение поля slug на основе значения поля name
    prepopulated_fields = {"slug": ("name",)}
    # Отображаемые поля в списке объектов
    list_display = ["name", "quantity", "price", "discount"]
    # Возможность редактировать скидку напрямую из списка объектов
    list_editable = ["discount",]
    # Поиск объектов по указанным полям
    search_fields = ["name", "description"]
    # Фильтрация объектов по указанным полям
    list_filter = ["discount", "quantity", "category"]
    # Порядок отображения полей в форме редактирования объекта
    fields = [
        "name",
        "category",
        "slug",
        "description",
        "image",
        ("price", "discount"),
        "quantity",
    ]
