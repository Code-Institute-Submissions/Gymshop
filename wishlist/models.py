from django.db import models
from profiles.models import UserProfile
from products.models import Product


class Wishlist(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    wished_item = models.ManyToManyField(Product)

    def __str__(self):
        return self.wished_item.name
