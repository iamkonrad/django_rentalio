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
        return str(self.username)

    def save(self, *args, **kwargs):
        if not self.username:                                                                                           #if no username, generating one
            username= slugify(f'{self.first_name} {self.last_name}')
            ex = self.__class__.objects.filter(username=username).exists()

            while ex:
                i=len(self.__class__.objects.filter(first_name=self.first_name, last_name=self.last_name))
                username = slugify(f'{self.first_name} {self.last_name}{i+1}')
                ex = self.__class__.objects.filter(username=username).exists()

            self.username=username
        super().save(*args,**kwargs)
