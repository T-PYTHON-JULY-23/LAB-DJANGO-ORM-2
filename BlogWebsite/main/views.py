from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from .models import BlogWebsite

# Create your views here.

def home_view(request:HttpRequest):

    blogs= BlogWebsite.objects.all()

    return render(request,"main/home_view.html", context = {"blogs" : blogs})

def add_blog_view(request: HttpRequest):

    if request.method == "POST":
        #adding a blog
        new_blog = BlogWebsite(title=request.POST["title"], content=request.POST["content"], category=request.POST["category"],  publish_date=request.POST["publish_date"])
        new_blog.save()

        return redirect("main:home_view")

    return render(request, "main/add_blog_view.html",{"Categorys": BlogWebsite.Categorys})

def blog_detail_view(request : HttpRequest, blog_id):
    
    #to get a single entry in the database
    blog = BlogWebsite.objects.get(id=blog_id)

    return render(request, "main/blog_detail.html", {"blog" : blog})

def blog_update_view(request:HttpRequest, blog_id):
    
    update_blog = BlogWebsite.objects.get(id=blog_id)

    #updating a book
    if request.method == "POST":
        update_blog.title = request.POST["title"]
        update_blog.content = request.POST["content"]
        update_blog.category = request.POST["category"]
        update_blog.publish_date = request.POST["publish_date"]
        update_blog.save()

        return redirect("main:blog_detail_view", blog_id=blog_id)

    return render(request, "main/update_blog.html", {"blog" : update_blog})

def blog_delete_view(request: HttpRequest, blog_id):
    #deleting an entry from database
    delete_blog = BlogWebsite.objects.get(id=blog_id)
    delete_blog.delete()

    return redirect("main:home_view")

def bolg_search(request: HttpRequest):

    if request.method == "POST":
        search_q = request.POST['search']
        posts= BlogWebsite.objects.filter(title= search_q)
        return render(request,"main/search.html",{'query':search_q,'posts':posts } )
    else:
        return render(request,"main/search.html",{})
