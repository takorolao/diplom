from django import template
from carts.models import Cart
from carts.utils import get_user_carts

# Регистрация модуля шаблонных тегов в Django
register = template.Library()

# Определение пользовательского тега "user_carts"
@register.simple_tag()
def user_carts(request):
    # Использование функции get_user_carts для получения корзин пользователя
    return get_user_carts(request)
