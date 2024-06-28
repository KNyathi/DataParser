from rest_framework import serializers
from .models import Applicant, Vacancy

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = '__all__'

class VacancySerializer(serializers.ModelSerializer):
    applicants = ApplicantSerializer(many=True, read_only=True)

    class Meta:
        model = Vacancy
        fields = '__all__'
