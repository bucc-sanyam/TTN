from django.db import models


# Create your models here.
class Publisher(models.Model):
    author = models.CharField(max_length=50)
    bookName = models.CharField(max_length=100)
