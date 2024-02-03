import re
from django import forms

# Определение формы для создания заказа
class CreateOrderForm(forms.Form):
    # Поля формы
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.ChoiceField(
        choices=[
            ("0", False),
            ("1", True),
        ],
    )
    delivery_address = forms.CharField(required=False)
    payment_on_get = forms.ChoiceField(
        choices=[
            ("0", 'False'),
            ("1", 'True'),
        ],
    )

    # Валидация номера телефона
    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']

        # Проверка, что номер телефона содержит только цифры
        if not data.isdigit():
            raise forms.ValidationError("Номер телефона должен содержать только цифры")
        
        # Проверка формата номера телефона (10 цифр)
        pattern = re.compile(r'^\d{10}$')
        if not pattern.match(data):
            raise forms.ValidationError("Неверный формат номера")

        return data