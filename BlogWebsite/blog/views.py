from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog


# Create your views here.


def add_post_view(request: HttpRequest):

    if request.method == "POST":
        #adding a post
        new_post = Blog(title=request.POST["title"], Content=request.POST["Content"], category= request.POST["category"], publish_date=request.POST["publish_date"])
        new_post.save()

        return redirect("blog:all_post_view")

    return render(request, 'blog/add_post.html',{"category_choices":Blog.category_choices})



def all_post_view(request: HttpRequest):

    blogs = Blog.objects.all()

    return render(request, "blog/all_post.html", context = {"blogs" : blogs})


def details_post_view(request:HttpRequest, blog_id):

    blog = Blog.objects.get(id=blog_id)

    return render(request,"blog/details_post.html",{"blog" : blog})


def update_post_view(request:HttpRequest,blog_id):
       
    blog = Blog.objects.get(id=blog_id)

    if request.method == "POST":
        blog.title = request.POST["title"]
        blog.Content = request.POST["Content"]
        blog.category = request.POST["category"]
        blog.publish_date = request.POST["publish_date"]
        blog.save()

        return redirect("blog:details_post_view", blog_id=blog.id)

    return render(request, "blog/update_post.html", {"blog": blog})


def delete_post_view(request:HttpRequest,blog_id):
    blog=Blog.objects.get(id=blog_id)
    blog.delete()

    return redirect("blog:all_post_view")