from django.contrib import admin

from .models import User, Book, Library, Author


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'user_name','password', 'date_of_membership', 'email']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['book_id', 'status', 'title', 'year_published', 'ISBN']


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    filter_horizontal = ['books', 'users']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['author_name', 'biography']
