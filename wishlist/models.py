from django.db import models
from profiles.models import UserProfile
from products.models import Product


class Wishlist(models.Model):
    user = models.ForeignKey(UserProfile, null=False, blank=False, on_delete=models.CASCADE)
    wished_item = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.wished_item.name
