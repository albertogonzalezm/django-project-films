import datetime

from django.db import models


# Create your models here.
class Film(models.Model):
    poster = models.ImageField(upload_to='filmPosters', default='')
    title = models.CharField(max_length=100, unique=True)
    synopsis = models.TextField(max_length=500)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    releaseDate = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=50)
    information = models.CharField(max_length=700, default='SOME STRING')
    image = models.ImageField(upload_to='directors')

    def __str__(self):
        return self.name
