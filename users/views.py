# Импорт необходимых модулей и классов
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from carts.models import Cart
from orders.models import Order, OrderItem

from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm

# Функция для обработки входа пользователя в систему.
def login(request):
    if request.method == 'POST':
        # Получение данных из формы входа
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            # Проверка подлинности пользователя
            user = auth.authenticate(username=username, password=password)

            session_key = request.session.session_key

            if user:
                # Авторизация пользователя и обновление корзины
                auth.login(request, user)
                messages.success(request, f"{username}, Вы вошли в аккаунт")

                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)

                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))
                    
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Home - Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)


# Функция для обработки регистрации нового пользователя.
def registration(request):
    if request.method == 'POST':
        # Получение данных из формы регистрации
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            # Сохранение нового пользователя
            form.save()

            session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)

            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)
            messages.success(request, f"{user.username}, Вы успешно зарегистрированы и вошли в аккаунт")
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()
    
    context = {
        'title': 'Home - Регистрация',
        'form': form
    }
    return render(request, 'users/registration.html', context)


# Защищенная функция для обработки профиля пользователя.
@login_required
def profile(request):
    if request.method == 'POST':
        # Обновление данных профиля пользователя
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Профайл успешно обновлен")
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)

    # Получение заказов пользователя с использованием предварительной загрузки связанных объектов.
    orders = Order.objects.filter(user=request.user).prefetch_related(
        Prefetch(
            "orderitem_set",
            queryset=OrderItem.objects.select_related("product"),
        )
    ).order_by("-id")

    context = {
        'title': 'Home - Кабинет',
        'form': form,
        'orders': orders,
    }
    return render(request, 'users/profile.html', context)


# Функция для отображения корзины пользователя.
def users_cart(request):
    return render(request, 'users/users_cart.html')


# Функция для обработки выхода пользователя из аккаунта.
@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('main:index'))
