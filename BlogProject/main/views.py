from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.
from .models import Post

def home(request:HttpRequest):
    return render(request, 'main/home.html')


def posts(request:HttpRequest):
    posts = Post.objects.all()
    return render(request, 'main/posts.html', {'posts': posts})

def add_post(request:HttpRequest):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        category = request.POST['category']
        publish_date = request.POST['publish_date']
        post = Post(title=title, content=content, category=category, publish_date=publish_date)
        post.save()
        return redirect('main:posts')
    return render(request, 'main/add_post.html', {"CATEGORY_CHOICES": Post.CATEGORY_CHOICES})

def detail_page(request : HttpRequest, post_id):
    
    #to get a single entry in the database
    post = Post.objects.get(id=post_id)

    return render(request, "main/detail_page.html", {"post" : post})

def update_post( request:HttpRequest, post_id):
    
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.category = request.POST["category"]
        post.publish_date = request.POST["publish_date"]
        post.save()

        return redirect("main:detail_post", post_id=post.id)

    return render(request, "main/update_post.html", {"post": post})

def delete_post(request: HttpRequest, post_id):
    #deleting an entry from database
    post = Post.objects.get(id=post_id)
    post.delete()

    return redirect("main:posts")




