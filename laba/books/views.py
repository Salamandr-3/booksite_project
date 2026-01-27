from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from .models import Book, CustomUser
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def index(request):
    featured_books = Book.objects.all()[:3]  # Получаем первые 3 книги для примера
    return render(request, 'books/index.html', {'featured_books': featured_books})

def catalog(request):
    books = Book.objects.all()
    return render(request, 'books/catalog.html', {'books': books})

def about(request):
    return render(request, 'books/about.html')

@ensure_csrf_cookie
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'redirect_url': '/'
                })
            messages.success(request, f'Добро пожаловать, {user.username}!')
            return redirect('index')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                errors = {}
                for field, field_errors in form.errors.items():
                    # Используем сообщения об ошибках из формы
                    errors[field] = field_errors[0]
                return JsonResponse({
                    'success': False,
                    'errors': errors
                })
            # Для обычных запросов оставляем стандартную обработку ошибок Django
    else:
        form = CustomUserCreationForm()
    return render(request, 'books/register.html', {'form': form})

@ensure_csrf_cookie
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'redirect_url': '/'
                })
            messages.success(request, f'Вход выполнен успешно! Добро пожаловать, {user.username}!')
            return redirect('index')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                errors = {}
                for field, field_errors in form.errors.items():
                    if field == '__all__':
                        # Используем первое сообщение об ошибке из списка
                        errors[field] = field_errors[0]
                    else:
                        # Для полей формы используем их собственные сообщения об ошибках
                        errors[field] = field_errors[0]
                return JsonResponse({
                    'success': False,
                    'errors': errors
                })
            # Для обычных запросов
            for field, errors in form.errors.items():
                for error in errors:
                    if field == '__all__':
                        messages.error(request, error)
                    else:
                        messages.error(request, f'{form.fields[field].error_messages.get("required", error)}')
    else:
        form = CustomAuthenticationForm(request=request)
    return render(request, 'books/login.html', {'form': form})

@login_required
def logout_view(request):
    username = request.user.username
    logout(request)
    messages.success(request, f'Вы успешно вышли из системы. До свидания, {username}!')
    return redirect('index')

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'books/book_detail.html', {'book': book})

def contacts(request):
    return render(request, 'books/contacts.html')

def test_static(request):
    """Тестовая страница для проверки статических файлов"""
    return render(request, 'books/test_static.html')
