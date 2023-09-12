from django.db import models
from books.models import Book
from django.utils.text import slugify

from rentals.choices import AGE_GROUPS


class Customer(models.Model):
    #Many To Many
    books=models.ManyToManyField(Book,blank=True, help_text='books currently rented out')

    first_name=models.CharField(max_length=300)
    last_name=models.CharField(max_length=300)
    age_group= models.CharField(
        max_length=5,
        choices=AGE_GROUPS,
        default='',
        blank=True,
    )
    username=models.CharField(max_length=300, blank=True, unique=True)
    additional_info=models.TextField(blank=True)
    rating=models.PositiveSmallIntegerField(default=50)
    book_count=models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"

    def save(self, *args, **kwargs):
        if not self.username:
            base_username = slugify(f'{self.first_name} {self.last_name}')
            unique_username = base_username
            i = 1

            while Customer.objects.filter(username=unique_username).exists():
                unique_username = f'{base_username}-{i}'
                i += 1

            self.username = unique_username

        super().save(*args, **kwargs)
