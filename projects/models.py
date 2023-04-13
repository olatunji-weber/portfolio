from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    img = models.ImageField(upload_to='pics')
    github_link = models.CharField(max_length=1020)

    def __str__(self):
        return self.title