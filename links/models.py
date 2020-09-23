from django.db import models

# Create your models here.
class Link(models.Model):
    url = models.URLField()
    name = models.TextField(unique=True)
    instant_redirect = models.BooleanField(default=False)

    def __str__(self):
        return self.name + " -> " + self.url

class Click(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.link.name + " at " + self.time.__str__()
