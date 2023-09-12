from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
from .models import Post

# Create your views here.
def home_view(request:HttpRequest):
    return render(request,'blog/home.html')

def add_post_view(request:HttpRequest):
  
  if request.method == 'POST':
      new_post = Post(title=request.POST['title'], content=request.POST['content'], category=request.POST['category'], publish_date=request.POST['publish_date'])
      new_post.save()
      return redirect("blog:all_posts_view")
  return render(request, 'blog/add_post.html')


def all_posts_view(request:HttpRequest):

    posts = Post.objects.all()

    return render(request, "blog/all_posts.html", context={"posts" : posts})

def post_detail_view(request:HttpRequest , post_id):
    
    blog = Post.objects.get(id=post_id)

def post_update_view(request:HttpRequest, post_id):
    category_list=[]
    post = Post.objects.get(id=post_id)

    if request.method=="POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.category = request.POST["category"]
        post.publish_date = request.POST["publish_date"]
        post.save()

        return redirect("blog:post_detail_view", post_id=post_id)
    return render(request,"blog/update_post.html", {"post" : post })

def post_delete_view(request:HttpRequest, post_id):
    blog = Post.objects.get(id=post_id)
    blog.delete()

    return redirect("blog:all_posts_view")
def search_view(request):
    if request.method == "POST":
        search_query = request.POST['search_query']
        posts = Post.objects.filter(title__contains=search_query)
    return render(request, "blog/all_posts.html", {'query':search_query, 'posts':posts})
