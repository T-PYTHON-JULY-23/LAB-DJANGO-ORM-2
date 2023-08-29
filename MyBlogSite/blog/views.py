from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.http import HttpRequest, HttpResponse

def home(request: HttpRequest):
    return render(request, 'blog/home.html')

def posts(request: HttpRequest):
    posts = Post.objects.all()
    return render(request, 'blog/posts.html', {'posts': posts})

def add_post(request: HttpRequest):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog:posts')  # Redirect to the posts page after successful submission
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})

def post_detail(request: HttpRequest, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_update(request, post_id):

    try:
        post = Post.objects.get(id=post_id)

        if request.method == "POST":
            post.title = request.POST["title"]
            post.content = request.POST["content"]
            post.category = request.POST["category"]
            post.publish_date = request.POST["publish_date"]
            post.photo = request.POST["photo"]
            post.save()
            return redirect('blog:posts')
    except:
        return render(request,'blog/notFound.html')
    return render(request, 'blog/post_update.html', {'post': post})


def post_delete(request:HttpRequest, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return render(request, 'blog/post_detail.html', {'post': post})

def search(request: HttpRequest):
    query = request.GET.get('query')
    if query:
        posts = Post.objects.filter(title__icontains=query)
    else:
        posts = []
    return render(request, 'blog/posts.html', {'posts': posts})
