from django.shortcuts import render , redirect,get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Post

# Create your views here. 

def home_view(request : HttpRequest):
    return render(request, "main/home.html")

def add_post_view(request: HttpRequest):
    if request.method == "POST":
        new_post = Post(title=request.POST["title"],  content =request.POST["content"],category =request.POST["category"],  publish_date =request.POST["publish_date"])
        new_post.save()
        return redirect("main:Posts_view")
    return render(request, 'main/add_post.html')



def Posts_view(request: HttpRequest):
    main = Post.objects.all()
    return render(request, "main/Posts.html", context = {"main" : main})


def post_detail_view(request : HttpRequest, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "main/post_detail.html", {"post" : post})



def post_update_view(request:HttpRequest, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.category = request.POST["category"]
        post.publish_date = request.POST["publish_date"]
        post.save()
        return redirect("main:post_detail_view", post_id=post.id)
    return render(request, "main/update_post.html", {"post": post})


def post_delete_view(request: HttpRequest, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect("main:Posts_view")


def search(request):
    if request.method == 'POST':
        search_query = request.POST['search_query']
        posts = Post.objects.filter(title__contains=search_query)
        return render(request, "main/Posts.html", {'query':search_query, 'posts':posts})
    