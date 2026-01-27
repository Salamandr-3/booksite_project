from django.db import models
from django.db.models import Manager
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    date_joined = models.DateTimeField(auto_now_add=True)
    
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

class Book(models.Model):
    objects: Manager = models.Manager()
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=200, default='books/img/book1.jpeg')

    def __str__(self) -> str:
        return str(self.title)
