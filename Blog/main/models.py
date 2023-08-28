from django.db import models

# Create your models here.

class Recipe(models.Model):

    title = models.CharField(max_length=2048)
    content = models.TextField()
    catagory=models.CharField(max_length=256)
    publish_date = models.DateField()