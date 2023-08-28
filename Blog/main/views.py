from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Recpie


# Create your views here.
def home(request: HttpRequest):

    return render(request, "main/home.html")


def addRecpie(request: HttpRequest):
     
     if request.method == "POST":
        #adding a recpes
        new_recpie = Recpie(title_recipes=request.POST['title_recipes'],category=request.POST['category'],Ingredients=request.POST['Ingredients'],Instructions=request.POST['Instructions'],publish_date=request.POST['publish_date'],image=request.FILES['image'])
        new_recpie.save()
        return redirect("main:post_view")

        

     return render(request, "main/addRecipe.html")

def all_recpies(request: HttpRequest):
    
    
   
    recpies = Recpie.objects.all()
    if request.method=="POST":
        serech_title=request.POST['search']
        c_category=request.POST['category']
        if serech_title!='':
          recpies=Recpie.objects.filter(title_recipes__startswith=serech_title)
        if c_category!='country of recpie':
          recpies=Recpie.objects.filter(category=c_category)
        
        
   
 
    return render(request, "main/post.html", context = {"recpies" : recpies})


def detail_recpie(request: HttpRequest,recpie_id):
   try:
    recpie = Recpie.objects.get(id=recpie_id)
   except:
     return render(request, "main/notfound.html")
   return render(request, "main/detail_recpie.html",{"recpie":recpie} )

def not_found(request: HttpRequest):

    return render(request, "main/notfound.html")

def update_recpie(request: HttpRequest,recpie_id):
    #updating recpie
    recpie = Recpie.objects.get(id=recpie_id)
    if request.method == "POST":
        recpie.title_recipes=request.POST['title_recipes']
        recpie.category=request.POST['category']
        recpie.Ingredients=request.POST['Ingredients']
        recpie.Instructions=request.POST['Instructions']
        recpie.publish_date=request.POST['publish_date']
        recpie.image=request.FILES['image']
        recpie.save()
        return redirect("main:post_view")
        

    return render(request, "main/update_recpie.html",{"recpie":recpie} )

def delete_recpie(request: HttpRequest,recpie_id):
    
    #deleting an entry from database
    recpie = Recpie.objects.get(id=recpie_id)
    recpie.delete()
    return redirect("main:post_view")

   