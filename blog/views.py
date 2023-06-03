from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from blog.forms import BlogForm, EditForm, CommentForm, SignupForm
from blog.models import Blog, Category
from django.contrib.auth import logout

from django.core.paginator import Paginator
# Create your views here.

def index_view(request):

    # blogs = Blog.objects.all()
    category=request.GET.get('category')

    if category == None:
        p = Paginator(Blog.objects.all(), 10)
        page = request.GET.get('page')
        blogs = p.get_page(page)
    else:
        p = Paginator(Blog.objects.filter(category__name=category), 10)
        page = request.GET.get('page')
        blogs=p.get_page(page)

    # p = Paginator(Blog.objects.all(), 10)
    # page = request.GET.get('page')
    # blogs = p.get_page(page)

    categories=Category.objects.all()

    return render(request, 'blog/index_view.html', {'blogs': blogs, 'categories': categories})

def about(request):
    return render(request, 'blog/about.html')

def new_view(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save()
            blog.created_by=request.user
            blog.save()
            return redirect('/')
    else:
        form=BlogForm()
    return render(request, 'blog/new_view.html', {'form': form})            


def detail_view(request, id):
    context = {}
    context["data"] = Blog.objects.get(id=id)
    return render(request, "blog/detail_view.html", context)



def update_view(request, id):
    
    context = {}
    
    obj = get_object_or_404(Blog, id=id)

    form = EditForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect('/')

    # context["form"] = form
    # context["obj"] = obj


    return render(request, "blog/update_view.html", {"form": form, "obj": obj})

def destroy_view(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect('/')

def search_blog(request):

    if request.method == "POST":
        search = request.POST['search']
        blogs = Blog.objects.filter(title__contains = search)
        return render(request, "blog/search_blog.html", {"search": search, "blogs": blogs})
    else:
        return render(request, "blog/search_blog.html", {})


def add_comment(request, id):
    if request.method == "POST":
        # blog = Blog.objects.get(id=id)
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form})
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'blog/signup.html', {
        'form': form
    })

def logout_user(request):
    logout(request)
    return redirect('/')
