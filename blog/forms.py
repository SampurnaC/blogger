from django import forms
from blog.models import Blog, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields=['title', 'description', 'category']
        widgets={
            'title': forms.TextInput(attrs= {'class': 'form-control'}),
            'description': forms.Textarea(attrs= {'class': 'form-control'}),
            'category': forms.Select(attrs= {'class': 'form-control'})


        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields=['title', 'description', 'category']
        widgets={
            'title': forms.TextInput(attrs= {'class': 'form-control'}),
            'description': forms.Textarea(attrs= {'class': 'form-control'}),
            'category': forms.Select(attrs= {'class': 'form-control'})


        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=['blog', 'body']
        widgets={
            'blog': forms.Select(attrs= {'class': 'form-control'}),
            'body': forms.Textarea(attrs= {'class': 'form-control'}),

        }

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
