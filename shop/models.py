from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class products(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = RichTextField()
    image = models.CharField(max_length=500)

# Create your models here.
