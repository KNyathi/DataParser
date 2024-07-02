from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Vacancy, Applicant

class VacancyTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.vacancy = Vacancy.objects.create(
            title='Python Developer',
            link='http://example.com',
            compensation='10 000 USD',
            experience='2 years',
            employer='Extreme Software Inc',
            location='New York'
        )

    def test_get_vacancies(self):
        response = self.client.get(reverse('vacancy-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Python Developer')

class ApplicantTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.applicant = Applicant.objects.create(
            title='Khayelihle Nyathi',
            link='http://example.com',
            age='23',
            status='Available',
            experience_duration='5 years',
            last_employer='Google Inc',
            last_position='Software Engineer',
            employment_dates='2015-2020'
        )

    def test_get_applicants(self):
        response = self.client.get(reverse('applicant-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Khayelihle Nyathi')
