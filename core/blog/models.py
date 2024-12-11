from django.db import models
from django.contrib.auth.models import User

# Create a class for posts in blog
class Post(models.Model):
    """ This is a class to define posts for blog application. """
    image = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.BooleanField(default=False)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()
    
    def __str__(self):
        return self.title

# Create a class for categories in blog
class Category(models.Model):
    """ This is a class to define categories for posts in blog application. """
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
