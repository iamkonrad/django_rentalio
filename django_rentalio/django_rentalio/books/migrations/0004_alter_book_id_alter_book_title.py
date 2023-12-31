# Generated by Django 4.2.4 on 2023-08-26 18:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.booktitle'),
        ),
    ]
