from django.db import models
import uuid
from django.urls import reverse
from django_countries.fields import CountryField

class Publisher(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=300)
    country= CountryField(blank_label='(select a country)')
    headquarters=models.CharField(max_length=100,blank=True)
    founded = models.PositiveIntegerField(blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} from {self.country}"

    def get_absolute_url(self):
        return reverse ('publishers:details', args=[self.name])
