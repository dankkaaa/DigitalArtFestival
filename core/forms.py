from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)

        labels = {
            "username": "Имя пользователя",
        }

        help_texts = {
            "username": "До 150 символов. Буквы, цифры и @/./+/-/_",
        }

    error_messages = {
        "password_mismatch": "Пароли не совпадают.",
    }