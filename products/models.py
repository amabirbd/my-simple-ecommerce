from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    #slug = models.SlugField()
    detail = models.TextField()
    category = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    photo = models.ImageField(blank=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.detail[:50] + '...'


@receiver(post_delete, sender=Product)
def submission_delete(sender, instance, **kwargs):
    instance.photo.delete(False)
