from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post
from django.http import Http404


# Create your views here.


def home(request:HttpRequest):
    
    return render(request,'blog/home.html')


def add_post(request:HttpRequest):
    if request.method == 'POST':
        new_post = Post(title=request.POST['title'], content=request.POST['content'], category=request.POST['category'], publish_date=request.POST['publish_date'])
        new_post.save()

        return redirect("blog:all_post_view")

    return render(request,'blog/add_post.html' , {"Post" : Post.category_choices})


def view_post(request:HttpRequest):
    posts = Post.objects.all().order_by('title')

    return render(request,'blog/all_post.html', context={'posts':posts} )


def detail_posts(request:HttpRequest, post_id):
    
    posts = Post.objects.get(id=post_id)

    return render (request,'blog/detail_posts.html', {'posts':posts})




    
        
    
        


def update_post(request:HttpRequest, post_id):
    
    

    try:
         posts = Post.objects.get(id=post_id)
         if request == 'POST':
            Post.title = request.POST['title']
            Post.content = request.POST['content']
            Post.category = request.POST['category']
            Post.publish_date = request.POST['publish_date']
            posts.save()

            return redirect('blog:detail_post_view', post_id=posts.id)
    except:

        return render(request,'blog/not_found.html')
        

    return render(request,'blog/ubdate_posts.html',{'posts':posts})




def delet_post(request:HttpRequest, post_id):
    posts = Post.objects.get(id=post_id)
    posts.delete()

    return redirect('blog:all_post_view')




def search_feature(request:HttpRequest):
    
    if 'search_query' in request.GET:
        
        posts = Post.objects.filter(title__contains=request.GET['search_query'])
    else:
        posts=Post.objects.all()

    return render(request, 'blog/search_result.html', {'posts':posts})
    


def category(request,post_choices):
    if request.method=='POSt':
        pass



    

