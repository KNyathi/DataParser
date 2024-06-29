# myapp/models.py

from django.db import models

class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    compensation = models.CharField(max_length=255)
    experience = models.CharField(max_length=100)
    employer = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Applicant(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    age = models.CharField(max_length=50)
    status = models.CharField(max_length=255)
    experience_duration = models.CharField(max_length=100)
    last_employer = models.CharField(max_length=255)
    last_position = models.CharField(max_length=255)
    employment_dates = models.CharField(max_length=255)

    def __str__(self):
        return self.title
