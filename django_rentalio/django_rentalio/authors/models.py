from django.db import models
from django.urls import reverse




class Author(models.Model):
    name = models.CharField(max_length=300)
    birth_year = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('authors:details', args=[self.name])

