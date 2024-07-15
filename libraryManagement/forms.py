from django import forms

from libraryManagement.models import Book
from user.models import User


class BorrowBookForm(forms.Form):
    book_id = forms.IntegerField()
    user_id = forms.IntegerField()


class CreateUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'address']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'ISBN', 'image', 'year_published', 'genre', 'status']
