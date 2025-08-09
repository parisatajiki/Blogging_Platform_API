from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=100)
    tags = models.JSONField(default=list, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)