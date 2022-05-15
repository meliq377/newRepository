from tabnanny import verbose
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    photo = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    photo1 = models.ImageField(upload_to='media/')
    photo2 = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.title




