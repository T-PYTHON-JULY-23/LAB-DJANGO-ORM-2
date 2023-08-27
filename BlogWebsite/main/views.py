from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse
from blog.models import Blog

# Create your views here.

def home_view(request : HttpRequest):


    return render(request, "main/index.html")



def Search_view(request:HttpRequest):
    blog=Blog.objects.filter(name__contains="blog")
    if request.method == "POST":
        blog.title = request.POST["title"]
        return redirect("{% url 'blog:details_post_view' blog.id %}")

    return render(request, "main/index.html", {"blog" : blog})
