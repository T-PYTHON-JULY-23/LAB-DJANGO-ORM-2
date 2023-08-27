from django.db import models

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('Technology', 'Technology'),
        ('Travel', 'Travel'),
        ('Food', 'Food'),
        ('Lifestyle', 'Lifestyle'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    publish_date = models.DateTimeField()
    #photo = models.ImageField(upload_to='post_photos/', null=True, blank=True)
    def __str__(self):
        return self.title
