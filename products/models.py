from django.db import models

class Product(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    #slug = models.SlugField()
    detail = models.TextField()
    category = models.CharField(max_length=100) 
    quantity = models.PositiveIntegerField()
    photo = models.ImageField( blank=True)
    
    def __str__(self):
        return self.title

    def snippet(self):
        return self.detail[:50] + '...'