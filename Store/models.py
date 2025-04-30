from django.db import models
from django.utils.text import slugify
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=100,null=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)  
        super().save(*args, **kwargs)
