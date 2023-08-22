import uuid

from django.db import models
from publishers.models import Publisher
from authors.models import Author
from django.utils.text import slugify


class BookTitle(models.Model):
    #FK
    publisher=models.ForeignKey(Publisher,on_delete=models.CASCADE)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)

    title = models.CharField(max_length=300,unique=True)
    slug=models.SlugField(blank=True)                                                                                   #optional
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Book position:{self.title}"

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
            super().save(*args,**kwargs)

class Book(models.Model):
    #FK
    title = models.ForeignKey(BookTitle,on_delete=models.CASCADE)
    book_id=models.CharField(max_length=50,blank=True)

    qr_code=models.ImageField(upload_to='qr_codes',blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

    def save(self,*args,**kwargs):
        if not self.book_id:
            self.book_id= str(uuid.uuid4()).replace('-','')[:30].lower()
        super().save(*args,**kwargs)

