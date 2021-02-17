from django.db import models
from profiles.models import UserProfile
from products.models import Product


class UserComments(models.Model):
    user = models.OneToOneField(UserProfile, null=False, blank=False, on_delete=models.CASCADE, related_name='usercomments')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE, related_name='products_comment')
    comment = models.TextField(null=False, blank=False)
    
    
    def __str__(self):
        return f'Comments ({self.user})'
