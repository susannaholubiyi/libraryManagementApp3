from django.contrib import admin

import user.models
from .models import Book, Library, Author


# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['book_id', 'status', 'title', 'year_published', 'ISBN']


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    filter_horizontal = ['books', 'users']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['author_name', 'biography']
