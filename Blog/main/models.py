from django.db import models

from django.db import models

# Create your models here.

class Post(models.Model):
    category_choices = (("Fashion", "Fashion"), ("Business", "Business"), ("Photography", "Photography"), ("Food", "Food"))

    title = models.CharField(max_length=2048)
    category = models.CharField(max_length=256)
    content = models.TextField()
    publish_date = models.DateTimeField()
