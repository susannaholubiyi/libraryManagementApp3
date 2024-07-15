from cloudinary.models import CloudinaryField
from django.db import models
from django.conf import settings


# Create your models here.

class Author(models.Model):
    author_id = models.AutoField(primary_key=True, unique=True)
    author_name = models.CharField(max_length=255)
    biography = models.TextField()

    def str(self):
        return f"{self.author_name}, {self.biography}"


class Book(models.Model):
    book_id = models.AutoField(primary_key=True, unique=True)
    STATUS = [
        ("B", "BORROWED"),
        ("AV", "AVAILABLE")
    ]
    GENRE = [
        ('R', 'ROMANCE'),
        ('C', 'COMEDY'),
        ('A', 'ACTION')
    ]
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    year_published = models.DateField()
    status = models.CharField(max_length=6, choices=STATUS, default="AV")
    genre = models.CharField(max_length=10, choices=GENRE, default='R')
    ISBN = models.CharField(max_length=13, unique=True)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    image = CloudinaryField('image', blank=True, null=True)

    def str(self):
        return f"{self.title}, {self.year_published},{self.status}, {self.ISBN}"


class Library(models.Model):
    books = models.ManyToManyField('Book', related_name='libraries')
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='libraries')

    def str(self):
        return f"{self.books}, {self.users}"
