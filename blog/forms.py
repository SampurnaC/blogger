from django import forms
from blog.models import Blog, Comment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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
        ordering = ['created_date']

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
        fields=['body']
        widgets={
            'blog': forms.Select(attrs= {'class': 'form-control'}),
            'body': forms.Textarea(attrs= {'class': 'form-control'}),

        }

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'form-control'
    }))
