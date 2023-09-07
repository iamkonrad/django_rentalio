import uuid
from django.db import models
from publishers.models import Publisher
from authors.models import Author
from django.utils.text import slugify
import qrcode
from django.urls import reverse
from io import BytesIO
from django.core.files import File
from PIL import Image
from rentals.choices import STATUS_CHOICES
from .utils import hash_book_info


class BookTitle(models.Model):
    #FK
    publisher=models.ForeignKey(Publisher,on_delete=models.CASCADE)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)

    title = models.CharField(max_length=300,unique=True)
    slug=models.SlugField(blank=True)                                                                                   #optional
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    @property
    def books(self):
        return self.book_set.all()

    def get_absolute_url(self):
        letter = self.title[:1].lower()
        return reverse("books:detail",kwargs={"letter":letter, "slug":self.slug})

    def __str__(self):
        return f"Book position:{self.title}"

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
            super().save(*args,**kwargs)

class Book(models.Model):
    #FK
    title = models.ForeignKey(BookTitle,on_delete=models.CASCADE)
    ISBN=models.CharField(max_length=20,blank=True)

    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4, editable=False)
    qr_code=models.ImageField(upload_to='qr_codes',blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        letter = self.title.title[:1].lower()
        return reverse("books:detail-book", kwargs={"letter": letter, "slug": self.title.slug, "book_id": self.id})

    def delete_objects(self):
        letter = self.title.title[:1].lower()
        return reverse('books:delete-book',kwargs={'letter':letter,'slug':self.title.slug,"book_id": self.id})


    def __str__(self):
        return str(self.title)

    @property
    def status (self):
        if len(self.rental_set.all()) >0:
            statuses = dict(STATUS_CHOICES)
            return statuses[self.rental_set.first().status]
        return False

    @property
    def rental_id(self):
        if len(self.rental_set.all()) > 0:
            return self.rental_set.first().id
        return None

    @property
    def is_available(self):
        if len(self.rental_set.all()) >0:
            status=self.rental_set.first().status
            return True if status == '#1' else False
        return True


    def save(self,*args,**kwargs):
        if not self.ISBN:
            self.ISBN= hash_book_info(self.title.title,self.title.publisher.name)

            qrcode_img=qrcode.make(self.ISBN)                                                                           #QR_CODE FUNCTIONALITY
            canvas = Image.new('RGB', (qrcode_img.pixel_size,qrcode_img.pixel_size), 'white')                           #qr code display canvas
            canvas.paste(qrcode_img)
            fname = f'qr_code-{self.ISBN}.png'                                                                          #file name
            buffer = BytesIO()
            canvas.save(buffer,'PNG')
            self.qr_code.save(fname,File(buffer),save=False)
            canvas.close()

        super().save(*args,**kwargs)