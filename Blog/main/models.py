from django.db import models


# Create your models here.

class post(models.Model):
    
    category_choices=(("Saudi Arabia " ,"Saudi Arabia") , ("Italy" , "Italy"), ("France", "France"), ("Spain", "Spain"), ("United States" ,"United States"  ))
    city = models.CharField(max_length=2048)
    content = models.TextField()
    category = models.CharField(max_length=128 , choices=category_choices)
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    publish_date = models.DateField()


class Comment(models.Model):

    rating_choices = ((1, "1 Star"), (2, "2 Star"), (3, "3 Star"), (4, "4 Star"), (5, "5 Star"), )

    post = models.ForeignKey(post, on_delete=models.CASCADE)
    name = models.CharField(max_length=512)
    content = models.TextField()
    rating = models.IntegerField(choices=rating_choices)
    created_at = models.DateTimeField(auto_now_add=True)

