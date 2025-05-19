from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Board, null=True, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    comment = models.TextField()
