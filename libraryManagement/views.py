from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from rest_framework import status, request
from rest_framework.decorators import api_view
from rest_framework.response import Response

from exception.exception import BookNotFoundException, UserNotFoundException, LoginFailedException
from .models import Book, User
from .serializers import BookSerializer
from .forms import BorrowBookForm


@api_view()
def view_all_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data, status.HTTP_200_OK)


@api_view(['POST'])
def borrow_book(request):
    if request.method == "POST":
        bookForm = BorrowBookForm(data=request.data)
        if bookForm.is_valid():
            book_id = bookForm.cleaned_data['book_id']
            user_id = bookForm.cleaned_data['user_id']
            try:
                book = Book.objects.get(id=book_id)
            except BookNotFoundException:
                return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

            try:
                user = User.objects.get(id=user_id)
            except UserNotFoundException:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
            if book.status != "AVAILABLE":
                return Response({"error": "Book already borrowed"}, status=status.HTTP_400_BAD_REQUEST)
            BorrowBookForm.objects.create(book=book, user=user)
            book.status = "BORROWED"
            book.save()
            user.number_of_books_borrowed += 1
            user.save()
            return Response("Book borrowed successfully", status=status.HTTP_201_CREATED)
        else:
            return Response(bookForm.errors, status=status.HTTP_400_BAD_REQUEST)
    bookForm = BorrowBookForm()
    return render(request, 'borrow_book.html', {'form': bookForm})


@api_view(["POST"])
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            user.is_signed_up = True
            messages.success(request, f'Account created for {user.username}!')
            return redirect('borrow_book')
    else:
        form = UserCreationForm()
    return render(request, 'signup_user.html', {'form': form})


@api_view(["POST"])
def login(request):
    if request.method == "POST":
        user_name = request.data.get("name")
        password = request.data.get("password")
        try:
            user = authenticate(user_name=user_name, password=password)
            if user is not None:
                login(request,user)
                messages.success(request, "Login successful")
                return redirect("borrow_book.html")
            else:
                messages.error(request, 'Invalid username or password.')
        except LoginFailedException as error:
            return render(request, 'login.html')

