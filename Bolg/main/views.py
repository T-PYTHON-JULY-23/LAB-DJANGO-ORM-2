from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import NewBlog
# Create your views here.
def home_page_view(request: HttpRequest):
    return render(request, "main/homePage.html")


def add_new_view(request: HttpRequest):

    if request.method == "POST":
        #adding a book
        new_book = NewBlog(title=request.POST["title"], content=request.POST["content"], category=request.POST["category"], publish_date=request.POST["publish_date"])
        new_book.save()

        return redirect("main:all_new_view")
    return render(request, 'main/add_new.html')

    
def all_new_view(request: HttpRequest):

    news = NewBlog.objects.all()

    return render(request, "main/all_new.html", context = {"news" : news})


def detail_view(request : HttpRequest, new_id):
    
    #to get a single entry in the database
    new = NewBlog.objects.get(id=new_id)

    return render(request, "main/detali.html", {"new" : new})


def updeat_view(request:HttpRequest, new_id):
    new = NewBlog.objects.get(id=new_id)
    if request.method == "POST":
        new.title = request.POST["title"]
        new.content = request.POST["content"]
        new.category = request.POST["category"]
        new.save()
        return redirect("main:all_new_view")
    return render(request, "main/updeat.html", {"new" : new})


def delete_view(request:HttpRequest , new_id):

    new = NewBlog.objects.get(id=new_id)
    new.delete()
    
    return redirect ("main:all_new_view")

def search_view(request):
    if request.method == "POST":
        search_query = request.POST['search_query']
        posts = NewBlog.objects.filter(title__contains=search_query)
    return render(request, "main/all_posts.html", {'query':search_query, 'posts':posts})
