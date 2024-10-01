from django.db import models

# Create your models here.
class Product (models.Model):
    productname = models.CharField(max_length=32)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    image = models.ImageField()
    stock = models.IntegerField()

    def __str__(self) -> str:
        return self.productname
