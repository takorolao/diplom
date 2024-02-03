from django.db.models import Q
from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    SearchHeadline,
)

from goods.models import Products
# Этот код определяет функцию q_search, которая выполняет поиск товаров в модели Products по заданному запросу


# Функция для выполнения поиска товаров
def q_search(query):
    # Если запрос состоит из цифр и не превышает 5 символов, ищем товары по ID
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))

    # Иначе используем поиск по вектору (name и description)
    vector = SearchVector("name", "description")
    query = SearchQuery(query)

    # Аннотируем ранг поиска
    result = (
        Products.objects.annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)
        .order_by("-rank")
    )

    # Аннотируем заголовок и описание с выделением искомых слов
    result = result.annotate(
        headline=SearchHeadline(
            "name",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel="</span>",
        )
    )
    result = result.annotate(
        bodyline=SearchHeadline(
            "description",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel="</span>",
        )
    )
    return result
