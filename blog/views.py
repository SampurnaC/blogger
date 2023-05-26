from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    posts = ['test1', 'test2', 'test3']  

    return render(request, 'blog/index.html', context={'posts': posts})

def about(request):
    return render(request, 'blog/about.html')
