from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories

# Представление для отображения главной страницы
def index(request):
    # Формирование контекста для передачи в шаблон
    context = {
        'title': 'Home - Главная',
        'content': "Магазин мебели HOME",
        'text_on_page': "Добро пожаловать в интернет-магазин мебели HOME, у нас вы найдете лучшее решение!"
    }

    # Отрисовка шаблона с передачей контекста
    return render(request, 'main/index.html', context)

# Представление для отображения страницы "О нас"
def about(request):
    # Формирование контекста для передачи в шаблон
    context = {
        'title': 'Home - О нас',
        'content': "О нас",
        'text_on_page': "Текст о том, почему этот магазин такой классный, и какой хороший товар."
    }

    # Отрисовка шаблона с передачей контекста
    return render(request, 'main/about.html', context)
