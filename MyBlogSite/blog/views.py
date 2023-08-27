from django.shortcuts import render, redirect,get_object_or_404
from .models import Post
from .forms import PostForm
from django.http import HttpRequest, HttpResponse

def home(request: HttpRequest):
    return render(request, 'blog/home.html')

def posts(request: HttpRequest):
    posts = Post.objects.all()
    return render(request, 'blog/posts.html', {'posts': posts})

def add_post(request:HttpRequest):
    if request.method == 'POST':
            new_blog = Post(title=request.POST["title"], author=request.POST["content"], category=request.POST["category"], publish_date=request.POST["publish_date"])
            new_blog.save()
            return redirect('posts')  # Redirect to the posts page after successful submission
    return render(request, 'blog/add_post.html', {'CATEGORY_CHOICES':Post.CATEGORY_CHOICES })

def post_detail(request: HttpRequest, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_update(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == "POST":
        post.title = request.POST["title"]
        post.category = request.POST["category"]
        post.publish_date = request.POST["publish_date"]
        post.save()
        return redirect('post_detail', post_id=post_id)
    return render(request, 'blog/post_update.html', {'post': post})


def post_delete(request:HttpRequest, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return render(request, 'blog/post_delete.html', {'post': post})

def search(request):
    query = request.GET.get('query')
    if query:
        posts = Post.objects.filter(title__icontains=query)
    else:
        posts = []
    return render(request, 'blog/posts.html', {'posts': posts})
