from django.db import models

class Author(models.Model):
    name = models.CharField(max_length = 255)
    designation = models.CharField(max_length = 256)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length = 255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    authors = models.ManyToManyField('Author')

    def __str__(self):
        return self.title
