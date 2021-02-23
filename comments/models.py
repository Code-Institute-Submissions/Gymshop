from django.db import models
from profiles.models import UserProfile
from products.models import Product


class UserComments(models.Model):
    """
    A model to connect a user to a product with a comment as a string/text
    """
    user = models.ForeignKey(UserProfile, null=False, blank=False, on_delete=models.CASCADE, related_name='usercomments')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE, related_name='products_comment')
    comment = models.TextField(null=False, blank=False)


    def __str__(self):
        return f'Comments ({self.product})'
