from django.shortcuts import render , redirect,get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Post, Comment

# Create your views here. 

def home_view(request : HttpRequest):
    return render(request, "main/home.html")

def add_post_view(request: HttpRequest):
    if request.method == "POST":
        new_post = Post(title=request.POST["title"],  content =request.POST["content"],category =request.POST["category"],image=request.FILES["image"],  publish_date =request.POST["publish_date"])
        new_post.save()
        return redirect("main:Posts_view")
    return render(request, 'main/add_post.html')



def Posts_view(request: HttpRequest):
    main = Post.objects.all()
    return render(request, "main/Posts.html", context = {"main" : main})


def post_detail_view(request : HttpRequest, post_id):
    
    #to get a single entry in the database
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post=post)

    if request.method == "POST":
        new_comment = Comment(post=post, name=request.POST["name"], content=request.POST["content"], rating=request.POST["rating"])
        new_comment.save()

    return render(request, "main/post_detail.html", {"post" : post, "comments" : comments, "Comment" : Comment})


def post_update_view(request:HttpRequest, post_id):
    try:
        post = Post.objects.get(id=post_id)
        if request.method == "POST":
            post.title = request.POST["title"]
            post.content = request.POST["content"]
            post.category = request.POST["category"]
            post.publish_date = request.POST["publish_date"]
            if "image" in request.FILES:
                post.image = request.FILES["image"]
                post.save()
                return redirect("main:post_detail_view", post_id=post.id)
    except:
        return render(request, "main/not_found.html")
    
    return render(request, "main/update_post.html", {"post": post})


def post_delete_view(request: HttpRequest, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect("main:Posts_view")


def posts_search_view(request: HttpRequest):

    if "search" in request.GET:
        main = Post.objects.filter(title__contains=request.GET["search"])
    else:
        main = Post.objects.all()

    return render(request, 'main/search.html', {"main" : main})
    