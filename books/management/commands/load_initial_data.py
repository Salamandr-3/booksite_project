
from django.core.management.base import BaseCommand
from books.models import Book

class Command(BaseCommand):
    help = 'Loads initial data for books'

    def handle(self, *args, **kwargs):
        if Book.objects.exists():
            return

        books_data = [
            {
                'title': 'Первая книга',
                'author': 'Автор 1',
                'description': 'Описание первой книги',
                'price': 999.99,
                'image': 'books/img/book1.jpeg'
            },
            {
                'title': 'Вторая книга',
                'author': 'Автор 2',
                'description': 'Описание второй книги',
                'price': 799.99,
                'image': 'books/img/book2.jpeg'
            },
            {
                'title': 'Третья книга',
                'author': 'Автор 3',
                'description': 'Описание третьей книги',
                'price': 599.99,
                'image': 'books/img/book3.jpeg'
            }
        ]

        for book_data in books_data:
            Book.objects.create(**book_data)
        
        self.stdout.write(self.style.SUCCESS('Successfully loaded initial data'))
