from django.db import models
from profiles.models import UserProfile
from products.models import Product


class UserComments(models.Model):
    user = models.OneToOneField(UserProfile, null=False, blank=False, on_delete=models.CASCADE, related_name='usercomments')
    products = models.ManyToManyField(Product, null=True, through='ProductComments')

    def __str__(self):
        return f'Comments ({self.user})'


class ProductComments(models.Model):
    comment = models.ForeignKey(UserComments, null=False, blank=False, on_delete=models.CASCADE, related_name='comment')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE, related_name='products_comment')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
