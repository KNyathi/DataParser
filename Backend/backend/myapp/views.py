from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Applicant, Vacancy
from .serializers import ApplicantSerializer, VacancySerializer

class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'surname', 'country_of_origin', 'native_language']
    search_fields = ['name', 'surname', 'country_of_origin', 'native_language']
    ordering_fields = ['name', 'surname', 'age']

class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'salary', 'region', 'required_experience', 'work_format', 'company']
    search_fields = ['title', 'skills', 'company']
    ordering_fields = ['title', 'salary', 'region']
