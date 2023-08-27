from django.db import models

# Create your models here.
class Recpie(models.Model):
    
    title_recipes = models.CharField(max_length=2048)
    category = models.CharField(max_length=2048)
    Ingredients = models.TextField()
    Instructions = models.TextField()
    publish_date = models.DateField()
    

