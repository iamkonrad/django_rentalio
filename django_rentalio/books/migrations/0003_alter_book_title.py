# Generated by Django 4.2.4 on 2023-08-22 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_rename_book_id_book_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_books', to='books.booktitle'),
        ),
    ]
