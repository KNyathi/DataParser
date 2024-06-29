from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Applicant, Vacancy
from .serializers import ApplicantSerializer, VacancySerializer

class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'age', 'status', 'experience_duration', 'last_employer', 'last_position']
    search_fields = ['title', 'age', 'status', 'experience_duration', 'last_employer', 'last_position']
    ordering_fields = ['title', 'age', 'experience_duration', 'last_employer', 'last_position']

class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'compensation', 'experience', 'employer', 'location']
    search_fields = ['title', 'compensation', 'experience', 'employer', 'location']
    ordering_fields = ['title', 'compensation', 'experience', 'employer', 'location']
