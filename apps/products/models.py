from django.contrib.auth import get_user_model
from django.db import models

user_model = get_user_model()


class Wishlist(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(user_model, on_delete=models.CASCADE)


class Product(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=12, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=2048, null=True, blank=True)
    wishlists = models.ManyToManyField(Wishlist, related_name="products")
