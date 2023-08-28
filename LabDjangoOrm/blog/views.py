from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from .models import Blog
# Create your views here.

def blog_view(request:HttpRequest):
    return render(request, 'base.html')

def all_blog_view(request:HttpRequest):
    blogs = Blog.objects.all()
    

    return render(request,'Posts.html',context = {"blogs":blogs})

def add_new_blog(request:HttpRequest):
    if request.method == "POST":
        new_blog = Blog(title=request.POST["title"],content=request.POST["content"],category=request.POST["category"],publish_date=request.POST["publish_date"])
        new_blog.save()
        return redirect("blog:all_blog_view")
    return render(request, 'Adding.html',{"category_choices": Blog.category_choices})


def blog_detail(request:HttpRequest,blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
        return render(request,'blog_detail.html',{"blog":blog})
    except Exception as e:
        return render(request,'exception.html')

def del_blog(request:HttpRequest, blog_id):
    blog=Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect("blog:all_blog_view")


def blog_update(request:HttpRequest,blog_id):
    blog = Blog.objects.get(id=blog_id)
    if request.method =="POST":
        blog.title = request.POST["title"]
        blog.content=request.POST["content"]
        blog.category=request.POST["category"]
        blog.publish_date=request.POST["publish_date"]
        blog.save()
        return redirect("blog:blog_detail", blog_id=blog.id)
    
    return render(request,'update_blog.html',{"blog":blog})
def search_blog(request:HttpRequest):
    
    if request.method == "POST":
        title_name=request.POST["search"]
        blogs = Blog.objects.filter(title__contains=title_name)
        return render(request,'Posts.html',context = {"blogs":blogs})


# def search_category(request:HttpRequest):
#     if request.method == "POST":
#         category=request.POST["category"]
#         blogs = Blog.objects.filter(category__contains=category)
#         return render(request,'Posts.html',context = {"blogs":blogs})

        





