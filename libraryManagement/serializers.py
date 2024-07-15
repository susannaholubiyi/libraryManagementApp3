from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['image', 'title', 'year_published', 'status', 'ISBN']
        read_only_fields = ['id', 'year_published']


