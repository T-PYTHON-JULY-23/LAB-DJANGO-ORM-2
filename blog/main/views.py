from django.shortcuts import render, redirect
from django.http import HttpRequest , HttpResponse 
from . import views
from .models import Post
# Create your views here.


def home_view(request : HttpRequest):

    return render(request,'main/home.html')

def add_view(request:HttpRequest):
    if request.method =='POST':
        new_post=Post(title=request.POST['title'],content=request.POST['content'],publish_date=request.POST['publish_date'],category=request.POST['category'])
        new_post.save()
        
    return render(request , 'main/add.html',{"category_choices":Post.category_choices})

def all_blogs_view(request:HttpRequest):
    posts = Post.objects.all()

    return render(request, "main/all_posts.html", context = {"posts" : posts})



def post_detail_view(request : HttpRequest, post_id):
    
    #to get a single entry in the database
    post = Post.objects.get(id=post_id)

    return render(request, "main/post_detail.html", {"post" : post})



def post_delete_view(request :  HttpRequest, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('main:home_view')


def post_update_view(request :HttpRequest, post_id ):
    
    post = Post.objects.get(id=post_id)

    #updating a post
    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.category = request.POST["category"]
        post.publish_date = request.POST["publish_date"]
        post.save()

        return redirect("main:post_detail_view", post_id=post.id)

    return render(request, "main/update_post.html", {"post": post})



def search_blogs_view(request : HttpRequest ):

    if request.method=='POST':
        user_query=request.POST['search_query']
        post=Post.objects.filter(title__contains=user_query)
        return render(request, "main/search.html", context = {"posts" : post})

    return redirect('main:home_view')
