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
        return reverse("books:detail",kwargs={"pk":self.pk})

    def __str__(self):
        return f"Book position:{self.title}"

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
            super().save(*args,**kwargs)

class Book(models.Model):
    #FK
    title = models.ForeignKey(BookTitle,on_delete=models.CASCADE)
    ISBN=models.CharField(max_length=50,blank=True)

    qr_code=models.ImageField(upload_to='qr_codes',blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

    def save(self,*args,**kwargs):
        if not self.ISBN:
            self.ISBN= str(uuid.uuid4()).replace('-','')[:24].lower()

            qrcode_img=qrcode.make(self.ISBN)                                                                           #QR_CODE FUNCTIONALITY
            canvas = Image.new('RGB', (qrcode_img.pixel_size,qrcode_img.pixel_size), 'white')                           #qr code display canvas
            canvas.paste(qrcode_img)
            fname = f'qr_code-{self.ISBN}.png'                                                                          #file name
            buffer = BytesIO()
            canvas.save(buffer,'PNG')
            self.qr_code.save(fname,File(buffer),save=False)
            canvas.close()

        super().save(*args,**kwargs)