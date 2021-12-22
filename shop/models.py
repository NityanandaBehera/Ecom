from django.db import models
from datetime import datetime
from django.db.models.deletion import CASCADE
from ckeditor.fields import RichTextField
""" from django.contrib.auth.models import User """

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
class Comment(models.Model):
    product=models.ForeignKey(products,related_name="comment",on_delete=CASCADE)
    """  commenter_name=models.ForeignKey(User) """
    commenter_name=models.CharField(max_length=100)
    comment_body=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s'%(self.product.title,self.commenter_name)


# Create your models here.
