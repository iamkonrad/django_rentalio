from django.core.management.base import BaseCommand
from authors.models import Author
from publishers.models import Publisher
from books.models import BookTitle,Book
from customers.models import Customer
from django_countries.fields import Country
import random

class Command(BaseCommand):

    help = "generate dummy data for testing purposes"

    def handle(self,*args,**kwargs):

        authors_list=['Quincy John','Wards Michael', 'Richards Ronald','Wang Anna']
        for name in authors_list:
            Author.objects.create(name=name)


        publishers_list = [
            {'name': 'Y publishing', 'country':Country(code='uk')},
            {'name': 'Bookera', 'country':Country(code='fr')},
            {'name': 'Bookzy', 'country':Country(code='de')},
            {'name': 'Publio', 'country':Country(code='us')},
        ]

        for item in publishers_list:
            Publisher.objects.create(**item)

        book_titles_list = ['Fiddler and the Hoof','1985','The Great Escape','Salman']
        publishers = [x.name for x in Publisher.objects.all()]
        items = zip(book_titles_list,publishers)

        for item in items:
            author = Author.objects.order_by('?')[0]
            publisher = Publisher.objects.get(name=item[1])
            BookTitle.objects.create(title=item[0],publisher=publisher,author=author)


        book_titles = BookTitle.objects.all()
        for title in book_titles:
            quantity = random.randint(1,5)
            for i in range(quantity):
                Book.objects.create(title=title)

        customers_list=[
            {'first_name':'John','last_name':'Doe'},
            {'first_name': 'Michael', 'last_name': 'Bird'},
            {'first_name': 'Maria', 'last_name': 'Berry'},
            {'first_name': 'Johan', 'last_name': 'Kreuz'},
        ]

        for item in customers_list:
            Customer.objects.create(**item)