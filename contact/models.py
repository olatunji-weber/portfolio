from django.db import models

# Create your models here.
class Contact(models.Model):
    fullName = models.CharField(max_length=256)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.CharField(max_length=1000)

def __str__(self):
    return (f"CONTACT: {self.fullName} - {self.email} \nMESSAGE: {self.message}")
