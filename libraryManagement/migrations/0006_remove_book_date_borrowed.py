# Generated by Django 5.0.6 on 2024-07-12 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryManagement', '0005_remove_book_borrower'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='date_borrowed',
        ),
    ]
