from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:product_id>', views.add_comment, name='add_comment'),
    path('delete/<int:product_id>', views.remove_comment, name='remove_comment')
]