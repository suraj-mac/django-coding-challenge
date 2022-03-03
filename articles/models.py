from django.db import models
from datetime import datetime


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey('authors.Author', on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.title} by {self.author}'

    def is_published(self):
        if self.published is None:
            return False
        if self.published > datetime.now():
            return False
        return True


class Genre(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f'{self.name}'
