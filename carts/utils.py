from carts.models import Cart

# Функция для получения корзин пользователя
def get_user_carts(request):
    # Проверка, аутентифицирован ли пользователь
    if request.user.is_authenticated:
        # Если пользователь аутентифицирован, возвращаем корзины пользователя, связанные с продуктами
        return Cart.objects.filter(user=request.user).select_related('product')
    
    # Если пользователь не аутентифицирован, и у сессии нет ключа, создаем новую сессию
    if not request.session.session_key:
        request.session.create()
    
    # Возвращаем корзины по сессии, связанные с продуктами
    return Cart.objects.filter(session_key=request.session.session_key).select_related('product')
