from django.db import models

class Post(models.Model):
    CATEGORY_CHOICES = (
        ('Technology', 'Technology'),
        ('Fashion', 'Fashion'),
        ('Travel', 'Travel'),
        ('Food', 'Food'),
        ('Sports', 'Sports'),
    )

    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title