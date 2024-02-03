from django.db import models
from goods.models import Products
from users.models import User

# Создаем класс QuerySet для удобства работы с запросами к модели Cart
class CartQueryset(models.QuerySet):
    
    # Метод для вычисления общей стоимости всех корзин в QuerySet
    def total_price(self):
        return sum(cart.products_price() for cart in self)
    
    # Метод для вычисления общего количества товаров во всех корзинах в QuerySet
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0

# Модель Cart представляет собой корзину товаров в интернет-магазине
class Cart(models.Model):
    # Внешний ключ на модель пользователя (может быть пустым, если пользователь не аутентифицирован)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    # Внешний ключ на модель товара в магазине
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Товар')
    # Количество товара в корзине
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')
    # Ключ сессии, связанный с анонимной корзиной (может быть пустым, если корзина привязана к пользователю)
    session_key = models.CharField(max_length=32, null=True, blank=True)
    # Дата и время создания корзины
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        db_table = 'cart'
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    # Использование созданного QuerySet в качестве менеджера объектов
    objects = CartQueryset().as_manager()

    # Метод для вычисления стоимости товаров в данной корзине
    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    # Метод для строкового представления объекта корзины
    def __str__(self):
        if self.user:
            return f'Корзина {self.user.username} | Товар {self.product.name} | Количество {self.quantity}'
        return f'Анонимная корзина | Товар {self.product.name} | Количество {self.quantity}'
