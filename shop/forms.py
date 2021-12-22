from django import forms
from django.forms.widgets import Widget
from . models import Comment
class commentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['commenter_name','comment_body']
        Widgets={
            'commenter_name':forms.TextInput(attrs={'class':'form-control'}),
            'comment_body':forms.Textarea(attrs={'class':'form-control'}),
        }

