from django.db import models

# Create your models here.


class Post(models.Model):
    category_choices = (('programing language','programing language'),('DataBase','DataBase'),('artificial intelligence','artificial intelligence'),('internet of things','internet of things'))

    title = models.CharField(max_length=2048)
    content = models.TextField()
    category = models.CharField(max_length=256 , choices=category_choices)
    publish_date =models.DateTimeField()
