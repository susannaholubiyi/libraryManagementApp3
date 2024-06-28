from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.AutoField(primary_key=True, unique=True)
    user_name = models.CharField(max_length=256)
    password = models.CharField(max_length=256, default='')
    email = models.EmailField(max_length=256)
    date_of_membership = models.DateTimeField(auto_now=True)
    number_of_books_borrowed = models.IntegerField(default=0)
    max_book_limit = models.IntegerField(default=3)
    address = models.CharField(max_length=255)
    is_signed_up = models.BooleanField(default=False)