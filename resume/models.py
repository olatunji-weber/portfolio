from django.db import models

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
    date = models.DateField()
    role = models.CharField(max_length=700)
    location = models.CharField(max_length=200)
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
        return (f"Role: {self.role}  - Date: {self.date} \nDetails: {self.details}")

class Education(models.Model):
    date = models.DateField()
    institution = models.CharField(max_length=256)
    course = models.CharField   (max_length=256)
    status = models.BooleanField()

    def __str__(self):
        return (f"Institution: {self.institution} - Date: {self.date} \nCourse: {self.course}")



