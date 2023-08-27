from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.db.models import Q

def home(request):
    return render(request, 'pages/home.html')

def posts(request):
    posts = Post.objects.all()
    return render(request, 'pages/posts.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        category = request.POST['category']
        
        if not title or not content or not category:
            error_message = 'Please fill in all required fields.'
            return render(request, 'pages/add_post.html', {'error_message': error_message})
        
        post = Post.objects.create(title=title, content=content, category=category)
        return redirect('post_detail', post_id=post.id)
    
        if not (title and content and category and publish_date):
            error_message = 'Please fill in all fields.'
            return render(request, 'add_post.html', {'error_message': error_message})
    return render(request, 'pages/add_post.html')

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'pages/post_detail.html', {'post': post})

def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.category = request.POST['category']
        post.save()
        return redirect('post_detail', post_id=post.id)
    return render(request, 'pages/update_post.html', {'post': post})

def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('posts')
    return render(request, 'pages/delete_post.html', {'post': post})

def search_posts(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(category__icontains=query)
        )
        return render(request, 'pages/posts.html', {'posts': posts})