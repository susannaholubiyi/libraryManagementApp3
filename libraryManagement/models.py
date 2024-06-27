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
    year_published = models.DateField()
    status = models.CharField(max_length=6, choices=STATUS, default="AV")
    genre = models.CharField(max_length=10, choices=GENRE, default='R')
    ISBN = models.CharField(max_length=13, unique=True)
    date_borrowed = models.DateTimeField(null=True, blank=True)
    borrower = models.ForeignKey(User, null=True, blank=True, related_name='borrowed_books',
                                 on_delete=models.SET_NULL)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True)

    def str(self):
        return f"{self.title}, {self.year_published},{self.status}, {self.ISBN}"


class Library(models.Model):
    books = models.ManyToManyField(Book, related_name='libraries')
    users = models.ManyToManyField(User, related_name='libraries')

    def str(self):
        return f"{self.books}, {self.users}"
