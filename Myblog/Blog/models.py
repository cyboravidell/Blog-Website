from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Post(models.Model):
    Sno = models.AutoField(primary_key=True)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=140)
    Timestamp = models.DateTimeField(blank=True)
    content = models.TextField()

    def __str__(self) -> str:
        return "Posted by "+ self.author + " - " + self.title

class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=TRUE)
    timestamp = models.DateTimeField(default=now)
    
