from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.description}"

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title} {self.author}"