from django.db import models

# Create your models here.
class Link(models.Model):
    link = models.URLField()
    name = models.TextField(unique=True)
    clicks = models.IntegerField()