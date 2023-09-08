from django.db import models
from django.urls import reverse
from django.utils.text import slugify



class Author(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('authors:details', args=[str(self.slug)])

