from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # Поле для хранения изображения пользователя (аватара).
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Аватар')
    
    # Поле для хранения номера телефона пользователя.
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    
    class Meta:
        # Настройки для модели User.
        db_table = 'user'  # Имя таблицы в базе данных.
        verbose_name = 'Пользователя'  # Имя модели в единственном числе.
        verbose_name_plural = 'Пользователи'  # Имя модели во множественном числе.

    def __str__(self):
        # Возвращает строковое представление пользователя, используя его имя пользователя.
        return self.username
