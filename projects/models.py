from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=700)

    def __str__(self):
        return (f"Project Title: {self.title} \nDescription: {self.description}")