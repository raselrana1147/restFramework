from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=191,blank=True)
    author_name = models.CharField(max_length=191,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
