from django.db import models

# Create your models here.

class Blog(models.Model):
    Bootcamps_ch = (("python" , "python"),("java" , "java"),("Data saince" , "Data saince"),("aws" , "aws"),)
    title= models.CharField(max_length=15)
    Content=models.TextField()
    publish_date = models.DateField()
    Bootcamp = models.CharField(max_length=128 , choices = Bootcamps_ch)




