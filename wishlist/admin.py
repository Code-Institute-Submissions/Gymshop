from django.contrib import admin
from .models import Wishlist
# Register your models here.


class WishListAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product',
    )

    ordering = ('user',)


admin.site.register(Wishlist, WishListAdmin)
