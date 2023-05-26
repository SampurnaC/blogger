from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.forms import BlogForm
from blog.models import Blog

# Create your views here.

def index(request):

    posts = ['test1', 'test2', 'test3']  

    return render(request, 'blog/index.html', context={'posts': posts})

def about(request):
    return render(request, 'blog/about.html')

def new(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/about')
    else:
        form=BlogForm()
    return render(request, 'blog/new.html', {'form': form})            
