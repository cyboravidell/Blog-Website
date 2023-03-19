from django.db import models

class Post(models.Model):
    Sno = models.AutoField(primary_key=True)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=140)
    Timestamp = models.DateTimeField(blank=True)
    content = models.TextField()

    def __str__(self) -> str:
        return "Posted by "+ self.author + " - " + self.title