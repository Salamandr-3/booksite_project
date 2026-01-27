from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from .models import CustomUser
from django.contrib.auth import authenticate
from django.db import models

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите email',
            'autocomplete': 'email'
        }),
        error_messages={
            'required': 'Пожалуйста, введите email',
            'invalid': 'Пожалуйста, введите корректный email',
            'unique': 'Этот email уже зарегистрирован'
        }
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите имя пользователя',
            'autocomplete': 'username'
        }),
        error_messages={
            'required': 'Пожалуйста, введите имя пользователя',
            'unique': 'Пользователь с таким именем уже существует',
            'invalid': 'Имя пользователя может содержать только буквы, цифры и символы @/./+/-/_'
        }
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите пароль',
            'autocomplete': 'new-password'
        }),
        error_messages={
            'required': 'Пожалуйста, введите пароль'
        }
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Подтвердите пароль',
            'autocomplete': 'new-password'
        }),
        error_messages={
            'required': 'Пожалуйста, подтвердите пароль'
        }
    )

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                "Пароли не совпадают",
                code='password_mismatch'
            )
        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "Этот email уже зарегистрирован",
                code='email_exists'
            )
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError(
                "Пользователь с таким именем уже существует",
                code='username_exists'
            )
        return username

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = 'Пароль должен содержать от 8 до 30 символов, включая букву и цифру'
        self.fields['password2'].help_text = 'Введите пароль повторно для подтверждения'

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите email или логин',
            'autocomplete': 'username'
        }),
        error_messages={
            'required': 'Пожалуйста, введите email или логин'
        }
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите пароль',
            'autocomplete': 'current-password'
        }),
        error_messages={
            'required': 'Пожалуйста, введите пароль'
        }
    )

    error_messages = {
        'invalid_login': 'Неверный логин/email или пароль. Пожалуйста, проверьте правильность ввода.',
        'inactive': 'Этот аккаунт неактивен.',
    }

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            # Пробуем найти пользователя по email или username
            try:
                user_obj = CustomUser.objects.get(
                    models.Q(email=username) | models.Q(username=username)
                )
                # Используем username для аутентификации
                self.user_cache = authenticate(
                    self.request,
                    username=user_obj.username,
                    password=password
                )
                if self.user_cache is None:
                    raise forms.ValidationError(
                        'Неверный пароль. Пожалуйста, проверьте правильность ввода.',
                        code='invalid_password'
                    )
            except CustomUser.DoesNotExist:
                raise forms.ValidationError(
                    'Пользователь с таким логином или email не найден. Проверьте правильность ввода или зарегистрируйтесь.',
                    code='invalid_login'
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data 