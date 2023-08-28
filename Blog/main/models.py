from django.db import models

# Create your models here.

class post(models.Model):
    
    category_choices=(("Saudi Arabia " ,"Saudi Arabia") , ("Italy" , "Italy"), ("France", "France"), ("Spain", "Spain"), ("United States" ,"United States"  ))
    title = models.CharField(max_length=2048)
    content = models.TextField()
    category = models.CharField(max_length=128 , choices=category_choices)
    publish_date = models.DateField()


