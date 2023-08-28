from django.db import models

# Create your models here.


class Blog(models.Model):
    category_choices=(("IT","IT"),("Physics","Physics"),("Chemistry","Chemistry"),("Medicine","Medicine"))
    title = models.CharField(max_length=2067)
    content = models.TextField()
    category = models.CharField(max_length=140,choices=category_choices)
    publish_date = models.DateTimeField()
