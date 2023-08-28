from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post

# Create your views here.


def blog_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        title_search_key = request.POST['search_key']
        posts = Post.objects.filter(title__contains = title_search_key)
    else:
        posts = Post.objects.all()
    
    return render(request, 'main/home.html', {"posts": posts})

def add_post_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        new_post = Post(title=request.POST["title"],
                        content=request.POST["content"],
                        category=request.POST["category"],
                        publish_date=request.POST["publish_date"])
        new_post.save()
        return redirect('main:blog_view')
    else:
        return render(request, 'main/add_post.html', {'post_category': Post.CATEGORY_CHOICES})


def post_detail_view(request: HttpRequest, post_id) -> HttpResponse:

    post = Post.objects.get(id=post_id)

    return render(request, 'main/post_detail.html', {"post": post})


def post_update_view(request: HttpRequest, post_id) -> HttpResponse:
    update_post = Post.objects.get(id=post_id)
    if request.method == "POST":
        update_post.title = request.POST['title']
        update_post.content = request.POST['content']
        update_post.category = request.POST['category']
        update_post.publish_date = request.POST['publish_date']
        update_post.save()
        return redirect('main:post_detail_view', post_id=update_post.id)
    else:
        # .isoFormat()
        #update_post.publish_date = update_post.publish_date.isoformat().replace("T", " ").split("+")[0]
        update_post.publish_date = update_post.publish_date.strftime("%Y-%m-%d %H:%M:%S")
        
        return render(request, 'main/update_post.html', {'post': update_post})


def post_delete_view(request: HttpRequest, post_id) -> HttpResponse:
    del_post = Post.objects.get(id=post_id)

    del_post.delete()

    return redirect('main:blog_view')
