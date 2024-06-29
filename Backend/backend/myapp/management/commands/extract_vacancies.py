# myapp/management/commands/extract_vacancies.py

from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import requests
from myapp.models import Vacancy

class Command(BaseCommand):
    help = 'Extract vacancies and store them in the database'

    def handle(self, *args, **kwargs):
        url = 'https://hh.ru/search/vacancy?text=python'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        vacancies = []

        for vacancy in soup.select('.vacancy-search-item__card'):
            title = vacancy.select_one('h2 .serp-item__title').text.strip()
            link = vacancy.select_one('h2 .serp-item__title-link-wrapper a')['href']
            compensation = vacancy.select_one('.compensation-text--kTJ0_rp54B2vNeZ3CTt2').text.strip()
            experience = vacancy.select_one('.label--rWRLMsbliNlu_OMkM_D3').text.strip()
            employer = vacancy.select_one('.company-info-text--vgvZouLtf8jwBmaD1xgp').text.strip()
            location = vacancy.select_one('[data-qa="vacancy-serp__vacancy-address_narrow"]').text.strip()

            vacancies.append({
                'title': title,
                'link': link,
                'compensation': compensation,
                'experience': experience,
                'employer': employer,
                'location': location,
            })

        for vacancy_data in vacancies:
            Vacancy.objects.update_or_create(
                link=vacancy_data['link'],
                defaults=vacancy_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully extracted and stored vacancies'))
