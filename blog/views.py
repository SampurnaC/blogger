from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from blog.forms import BlogForm, EditForm
from blog.models import Blog

# Create your views here.

def index_view(request):

    blogs = Blog.objects.all()

    return render(request, 'blog/index_view.html', {'blogs': blogs})

def about(request):
    return render(request, 'blog/about.html')

def new_view(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=BlogForm()
    return render(request, 'blog/new_view.html', {'form': form})            


def detail_view(request, id):
    context = {}
    context["data"] = Blog.objects.get(id=id)
    return render(request, "blog/detail_view.html", context)



# def edit(request, id):

#     blog = Blog.objects.get(id=id)
#     return render(request, 'blog/edit.html', {'blog': blog})

# def update(request, id):

#     blog = Blog.objects.get(id=id)
#     breakpoint()

#     form = BlogForm(request.POST, instance=blog)
    
#     if form.is_valid():
#         form.save()
#         return redirect('/')
#     return render(request, 'blog/edit.html', {'form': form})


def update_view(request, id):
    
    context = {}
    
    obj = get_object_or_404(Blog, id=id)

    form = EditForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect('/')

    # context["form"] = form
    # context["obj"] = obj


    return render(request, "blog/update_view.html", {"form": form})

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
