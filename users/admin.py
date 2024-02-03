from django.contrib import admin
from carts.admin import CartTabAdmin
from orders.admin import OrderTabulareAdmin

from users.models import User

# Регистрация модели User в админке
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "email",]
    search_fields = ["username", "first_name", "last_name", "email",]

    # Добавление инлайна для корзин и заказов пользователя
    inlines = [CartTabAdmin, OrderTabulareAdmin]
