from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField()
    category = models.CharField(max_length=100) 
    quantity = models.PositiveIntegerField()
    
    def __str__(self):
        return self.title