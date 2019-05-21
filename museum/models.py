from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Exhibit(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Object(models.Model):
    exhibit = models.ForeignKey(Exhibit, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    image = models.ImageField(upload_to='objects/', blank=True)

    def __str__(self):
        return self.name
