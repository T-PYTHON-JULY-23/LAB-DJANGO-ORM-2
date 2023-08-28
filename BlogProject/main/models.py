from django.db import models

# Create your models here.
class Post(models.Model):
    CATEGORY_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('healthy_desserts', 'Healthy Desserts'),
        ('dinner', 'Dinner'),
        ('lunch', 'Lunch'),
        ('snacks', 'Snacks'),
    ]

    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    publish_date = models.DateTimeField()

    def __str__(self):
        return self.title

