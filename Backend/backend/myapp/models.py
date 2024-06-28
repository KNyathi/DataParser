from django.db import models

class Applicant(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    country_of_origin = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    native_language = models.CharField(max_length=50)
    foreign_languages = models.CharField(max_length=200)
    work_experience = models.TextField()
    education = models.TextField()

    def __str__(self):
        return f"{self.name} {self.surname}"

class Vacancy(models.Model):
    JOB_EXPERIENCE_CHOICES = [
        ('no_experience', 'No experience'),
        ('1_to_3_years', 'From 1 to 3 years'),
        ('3_to_6_years', 'From 3 to 6 years'),
        ('more_than_6_years', 'More than 6 years'),
    ]

    WORK_FORMAT_CHOICES = [
        ('full_time', 'Full time'),
        ('part_time', 'Part time'),
        ('remote', 'Remote'),
    ]

    title = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    region = models.CharField(max_length=100)
    required_experience = models.CharField(max_length=20, choices=JOB_EXPERIENCE_CHOICES)
    work_format = models.CharField(max_length=20, choices=WORK_FORMAT_CHOICES)
    skills = models.TextField()
    company = models.CharField(max_length=100)
    applicants = models.ManyToManyField(Applicant, related_name='vacancies')

    def __str__(self):
        return self.title
