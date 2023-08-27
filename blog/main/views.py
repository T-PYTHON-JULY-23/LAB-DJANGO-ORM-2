from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Post

def home_view(request: HttpRequest):

    return render(request, "main/home.html")

def add_post_view(request: HttpRequest):
    if request.method == "POST":
        new_post = Post(title=request.POST["title"], content=request.POST["content"], category=request.POST["category"], publish_date=request.POST["publish_date"])
        new_post.save()

        return redirect("main:all_posts_view")

    return render(request, 'main/add_post.html')



def all_posts_view(request: HttpRequest):
    posts = Post.objects.all()
    

    return render(request, "main/posts.html", context = {"posts" : posts})

def post_detail_view(request: HttpRequest,post_id):

    post = Post.objects.get(id=post_id)

    return render(request, "main/post_detail.html", context = {"post" : post})

def update_view(request: HttpRequest,post_id):

    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.category = request.POST["category"]
        post.publish_date = request.POST["publish_date"]
        post.save()

        return redirect("main:post_detail_view", post_id= post.id)

    return render(request, "main/update_post.html",{"post" : post})

def delete_view(request: HttpRequest,post_id):

    post = Post.objects.get(id=post_id)
    post.delete()

    return redirect("main:all_posts_view")

# def filter_view(request:HttpRequest):
#     if request.method == "POST":
#         user_input = request.POST['user_input']
#         post = Post.objects.filter(title__contains=user_input)


#     return render("main/filter_post.html",{"post" : post,})