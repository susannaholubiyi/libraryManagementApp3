from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class BorrowBookForm(forms.Form):
    book_id = forms.IntegerField()
    user_id = forms.IntegerField()
