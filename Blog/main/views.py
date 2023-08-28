from django.shortcuts import render ,redirect
from django.http import HttpResponse , HttpRequest
from .models import Recipe

# Create your views here.

def home_view(request):

    return render(request , 'main/home.html')

def add_post(request):
    if request.method == "POST":
        #adding a Recipe
        new_Recipe = Recipe(title=request.POST["title"], content=request.POST["content"], catagory=request.POST["catagory"], publish_date=request.POST["publish_date"])
        new_Recipe.save()
        return redirect("main:all_recipes_view")
    return render(request,('main/add_post.html'))

def all_recipes_view(request: HttpRequest):

    recipes = Recipe.objects.all()

    return render(request, "main/all_Recipes.html", context = {"recipes" : recipes})

'''------------detail page--------------------------------------'''

def recipe_detail_view(request : HttpRequest, recipe_id):
    
    recipe= Recipe.objects.get(id=recipe_id)

    return render(request, "main/recipe_detail.html", {"recipe" : recipe})

'''------------------------------------------------'''
def recipe_update_view(request:HttpRequest, recipe_id):
    
    recipe = Recipe.objects.get(id=recipe_id)

    #updating a recipe
    if request.method == "POST":
        recipe.title = request.POST["title"]
        recipe.content = request.POST["content"]
        recipe.catagory = request.POST["catagory"]
        recipe.publish_date = request.POST["publish_date"]
        recipe.save()

        return redirect("main:recipe_detail_view", recipe_id=recipe.id)

    return render(request, "main/update_recipe.html", {"recipe": recipe})


def recipe_delete_view(request: HttpRequest, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    recipe.delete()

    return redirect("main:all_recipes_view")
