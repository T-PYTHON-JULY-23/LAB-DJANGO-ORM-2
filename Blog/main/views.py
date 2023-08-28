from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import post

# Create your views here.

def home_view(request : HttpRequest):
        
    
    
    return render(request,"main/index.html")

def about_view(request: HttpRequest):

    return render(request, "main/about.html")

def dark_view(request:HttpRequest):

    #setting a cookie   
    response = redirect("main:home_view")
    response.set_cookie("mode", "dark")

    return response

def light_view(request:HttpRequest):
    
    #setting a cookie
    response = redirect("main:home_view")
    response.set_cookie("mode", "light")

    return response
def add_post(request: HttpRequest):

    if request.method == "POST":
        #adding a post
        new_post = post(title=request.POST["title"], content=request.POST["content"], category= request.POST["category"], publish_date=request.POST["publish_date"])
        new_post.save()

        return redirect("main:all_posts")

    return render(request, 'main/add_post.html')
      

def all_posts(request: HttpRequest):
    if request.GET.get('search'):
        posts=post.objects.filter(title__contains="search")
    else:
        posts = post.objects.all()

    return render(request, "main/all_posts.html", context = {"posts" : posts})



def post_detail_view(request : HttpRequest, post_id):
    
    #to get a single entry in the database
    posts = post.objects.get(id=post_id)

    return render(request, "main/post_detail.html", {"post" : posts})



def post_update_view(request:HttpRequest, post_id):
    
    posts = post.objects.get(id=post_id)

    #updating a post
    if request.method == "POST":
        posts.title = request.POST["title"]
        posts.content = request.POST["content"]
        posts.category = request.POST["category"]
        posts.publish_date = request.POST["publish_date"]
        posts.save()

        return redirect("main:post_detail_view", post_id=posts.id)

    return render(request, "main/update_post.html", {"post": posts})


def post_delete_view(request: HttpRequest, post_id):
    #deleting an entry from database
    posts = post.objects.get(id=post_id)
    posts.delete()
    return redirect ("main:all_posts")


