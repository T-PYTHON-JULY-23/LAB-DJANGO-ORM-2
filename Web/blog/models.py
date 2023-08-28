from django.db import models

# Create your models here.

class Post(models.Model):

    category_choices = (("Lifestyle", "Lifestyle Blog"), ("Sports", "Sports Blog"),("Music", "Music Blog"),("Travel", "Music Blog"),)
    title = models.CharField(max_length=2044)
    content = models.TextField()
    category = models.CharField(max_length=2044, choices=category_choices)
    publish_date = models.DateTimeField()