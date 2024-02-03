from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from carts.models import Cart
from carts.utils import get_user_carts

from goods.models import Products

# Функция добавления товара в корзину
def cart_add(request):
    # Получение идентификатора продукта из POST-запроса
    product_id = request.POST.get("product_id")
    # Получение объекта продукта из базы данных
    product = Products.objects.get(id=product_id)
    # Проверка, аутентифицирован ли пользователь
    if request.user.is_authenticated:
        # Если пользователь аутентифицирован, ищем корзины пользователя для данного продукта
        carts = Cart.objects.filter(user=request.user, product=product)
        # Если корзина уже существует, увеличиваем количество продукта, иначе создаем новую корзину
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)

    else:
        # Если пользователь не аутентифицирован, работаем с корзинами по сессии
        carts = Cart.objects.filter(
            session_key=request.session.session_key, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(
                session_key=request.session.session_key, product=product, quantity=1)
    # Обновление данных корзины пользователя и формирование HTML-кода для отображения в интерфейсе
    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": user_cart}, request=request)
    # Формирование данных для ответа в формате JSON
    response_data = {
        "message": "Товар добавлен в корзину",
        "cart_items_html": cart_items_html,
    }

    return JsonResponse(response_data)
            
# Функция изменения количества товара в корзине
def cart_change(request):
    # Получение идентификатора корзины и нового количества из POST-запроса
    cart_id = request.POST.get("cart_id")
    quantity = request.POST.get("quantity")
    # Обновление количества товара в корзине
    cart = Cart.objects.get(id=cart_id)

    cart.quantity = quantity
    cart.save()
    updated_quantity = cart.quantity
    
    # Обновление данных корзины пользователя и формирование HTML-кода для отображения в интерфейсе
    cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": cart}, request=request)
    # Формирование данных для ответа в формате JSON
    response_data = {
        "message": "Количество изменено",
        "cart_items_html": cart_items_html,
        "quaantity": updated_quantity,
    }

    return JsonResponse(response_data)


# Функция удаления товара из корзины
def cart_remove(request):
    # Получение идентификатора корзины из POST-запроса
    cart_id = request.POST.get("cart_id")
    # Удаление корзины и получение количества удаленного товара
    cart = Cart.objects.get(id=cart_id)
    quantity = cart.quantity
    cart.delete()
    # Обновление данных корзины пользователя и формирование HTML-кода для отображения в интерфейсе
    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": user_cart}, request=request)
    # Формирование данных для ответа в формате JSON
    response_data = {
        "message": "Товар удален",
        "cart_items_html": cart_items_html,
        "quantity_deleted": quantity,
    }

    return JsonResponse(response_data)