from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Manager

class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=True)


class Book(models.Model):
    objects: Manager = models.Manager()
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=200, default='books/img/book1.jpeg')

    def __str__(self) -> str:
        return str(self.title)
