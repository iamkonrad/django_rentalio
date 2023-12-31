# Generated by Django 4.2.4 on 2023-09-13 03:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_alter_book_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ISBN',
            field=models.CharField(blank=True, max_length=13),
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=32, primary_key=True, serialize=False),
        ),
    ]
