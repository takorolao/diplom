from django import template
from django.utils.http import urlencode
from goods.models import Categories

# Регистрация модуля шаблонных тегов в Django
register = template.Library()

# Пользовательский тег для получения всех категорий товаров
@register.simple_tag()
def tag_categories():
    return Categories.objects.all()

# Пользовательский тег для изменения параметров URL
@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    # Получение текущих параметров из контекста запроса
    query = context['request'].GET.dict()
    
    # Обновление параметров запроса новыми значениями
    query.update(kwargs)
    
    # Возврат строки с параметрами в виде URL-кодировки
    return urlencode(query)
