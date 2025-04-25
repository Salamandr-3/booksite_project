
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Book, User

def index(request):
    featured_books = Book.objects.all()[:3]  # Получаем первые 3 книги для примера
    return render(request, 'books/index.html', {'featured_books': featured_books})

def catalog(request):
    books = Book.objects.all()
    return render(request, 'books/catalog.html', {'books': books})

def about(request):
    return render(request, 'books/about.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, password=password, email=email)
            login(request, user)
            return redirect('index')
            
    return render(request, 'books/register.html')

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'books/book_detail.html', {'book': book})

def contacts(request):
    return render(request, 'books/contacts.html')
