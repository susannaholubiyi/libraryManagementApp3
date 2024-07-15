from django.contrib.auth.models import AbstractUser
from django.db import models

from libraryManagement.models import Book


# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11, unique=True)
    date_of_membership = models.DateTimeField(auto_now=True)
    number_of_books_borrowed = models.IntegerField(default=0)
    max_book_limit = models.IntegerField(default=3)
    address = models.CharField(max_length=255)


class BorrowBook(User):
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    date_borrowed = models.DateTimeField(auto_now_add=True)
