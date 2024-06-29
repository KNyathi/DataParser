# myapp/admin.py
from django.contrib import admin
from .models import Applicant, Vacancy

admin.site.register(Applicant)
admin.site.register(Vacancy)
