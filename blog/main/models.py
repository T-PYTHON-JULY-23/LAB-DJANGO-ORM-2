from django.db import models

# Create your models here.
class Blog(models.Model):
    

    category_choices = (
    ("Lifestyle", "Lifestyle"),
    ("Beauty", "Beauty"),
    ("Fashion", "Fashion"),
   
)
    title=models.CharField(max_length=256)
    content=models.TextField()
    category=models.CharField(max_length=10, choices=category_choices)
    publish_date =models.DateTimeField()
