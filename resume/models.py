from django.db import models
from datetime import date

# Create your models here.
class Skill(models.Model):
    skill = models.CharField(max_length=256)      

    def __str__(self):
        return self.skill

class Language(models.Model):
    language = models.CharField(max_length=256)

    def __str__(self):
        return self.language

class Experience(models.Model):
    startDate = models.DateField(default=date(2001,9,7))
    endDate = models.DateField(default=date(2007,9,27))
    role = models.CharField(max_length=700)
    organization = models.CharField(max_length=256, default="SARCS")
    location = models.CharField(max_length=200, default="Remote")
    details = models.CharField(max_length=700)
    status = models.BooleanField()

    # def __init__(self, date, role, location, details, status):
    #     #signifies the date of commencement in this role
    #     self.date = date
    #     #This signifies the role for this particular experience
    #     self.role = role
    #     #Location states the city and country of the role - it could also be Remote
    #     self.locatiion = location
    #     #Details describes the work done in the role
    #     self.details = details
    #     #Status helps to signify if the user is currently working in this role of not
    #     if status.upper() == "ONGOING":
    #         self.status = True
    #     elif status.upper() == "ENDED":
    #         self.status = False

    def __str__(self):
        return (f"Role: {self.role} - Organization: {self.organization} \nDetails: {self.details}")

class Education(models.Model):
    startDate = models.DateField(default=date(2001,9,7))
    endDate = models.DateField(default=date(2007,9,27))
    institution = models.CharField(max_length=256)
    location = models.CharField(max_length=500)
    degree = models.CharField(max_length=256)
    fieldOfStudy = models.CharField(max_length=256, default="Computer Science")
    status = models.BooleanField()

    def __str__(self):
        return (f"Institution: {self.institution} - {self.location}   \nCourse: {self.fieldOfStudy}")



