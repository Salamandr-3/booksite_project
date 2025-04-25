
from django.shortcuts import render
from .models import Book

def index(request):
    featured_books = Book.objects.all()[:3]  # Получаем первые 3 книги для примера
    return render(request, 'books/index.html', {'featured_books': featured_books})

def catalog(request):
    books = Book.objects.all()
    return render(request, 'books/catalog.html', {'books': books})

def about(request):
    return render(request, 'books/about.html')

def register(request):
    return render(request, 'books/register.html')

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'books/book_detail.html', {'book': book})

def contacts(request):
    return render(request, 'books/contacts.html')
