from django.db import models
from django.urls import reverse




class Author(models.Model):
    name = models.CharField(max_length=300)
    birth_year = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('authors:details', args=[self.name])

    @property
    def formatted_name(self):
        name_parts = self.name.split()
        if len(name_parts) >= 2:
            return f"{name_parts[-1]}, {' '.join(name_parts[:-1])}"
        return self.name
