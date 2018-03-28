from django.db import models

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length = 140)
    query = models.TextField()
    contact = models.CharField(max_length = 140)

    def __str__(self):
        return self.name