from django import forms

from .models import UserComments

# no idea 
class CommentForm(forms.ModelForm):

    class Meta:
        model = UserComments
        fields = ('comment',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

