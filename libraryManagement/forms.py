from django import forms

from libraryManagement.models import User


class BorrowBookForm(forms.Form):
    book_id = forms.IntegerField()
    user_id = forms.IntegerField()


class CreateUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['user_name', 'email', 'password', 'address']
