from django import forms

from .models import UserComments


class CommentForm(forms.ModelForm):
    """ A form that only allows users to add a comment to the model """
    class Meta:
        model = UserComments
        fields = ('comment',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
