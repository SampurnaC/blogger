from django import forms
from blog.models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields="__all__"

class EditForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields="__all__"
