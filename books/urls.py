
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('contacts/', views.contacts, name='contacts'),
]
