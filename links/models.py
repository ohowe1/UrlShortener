from django.db import models

# Create your models here.
class Link(models.Model):
    url = models.URLField()
    name = models.TextField(unique=True)
    clicks = models.IntegerField(default=0, auto_created=True)

    def __str__(self):
        return self.name + " -> " + self.url