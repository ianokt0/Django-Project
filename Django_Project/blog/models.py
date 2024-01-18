from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=65, blank=True, null=True)
    body = models.TextField()
    email = models.EmailField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    category = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return "{}. {}".format(self.id, self.title)
