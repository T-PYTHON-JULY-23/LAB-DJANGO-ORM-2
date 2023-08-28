from django.db import models
# Create your models here.

class Post(models.Model):

    category_choices = (("Misc", "Miscellenous"), ("Bio", "Biography"), ("Fantasy", "Fantasy"), ("Novel", "Novel"))

    title=models.CharField(max_length=256)
    content=models.TextField()
    publish_date =models.DateTimeField()
    category = models.CharField(max_length=128, choices=category_choices)

    