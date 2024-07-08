# Generated by Django 5.0.6 on 2024-07-08 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryManagement', '0002_book_genre_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('B', 'BORROWED'), ('AV', 'AVAILABLE'), ('NA', 'NOT_AVAILABLE')], default='AV', max_length=6),
        ),
        migrations.AlterField(
            model_name='user',
            name='number_of_books_borrowed',
            field=models.IntegerField(default=3),
        ),
    ]