from django.db import models

# Create your models here.

class Blog(models.Model):

    category_choices=(("food","food"),("health","health"),("care and beauty","care and beauty"),("fitness","fitness"))

    title = models.CharField(max_length=2048,null=True)
    Content = models.TextField()
    category = models.TextField(max_length=128 ,choices=category_choices)
    publish_date = models.DateField()

    




