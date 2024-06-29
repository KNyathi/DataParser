# myapp/management/commands/extract_vacancies.py
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import requests
from myapp.models import Vacancy

class Command(BaseCommand):
    help = 'Scrape data from hh.ru for vacancies'

    def handle(self, *args, **kwargs):
        url = "https://hh.ru/search/vacancy?text=python&area=1&salary=&currency_code=RUR&experience=all&order_by=relevance&search_period=all"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            for vacancy_div in soup.find_all('div', {'class': 'vacancy-serp-item'}):
                title = vacancy_div.find('a', {'data-qa': 'vacancy-serp__vacancy-title'}).text.strip()
                employer = vacancy_div.find('a', {'data-qa': 'vacancy-serp__vacancy-employer'}).text.strip() if vacancy_div.find('a', {'data-qa': 'vacancy-serp__vacancy-employer'}) else ''
                compensation = vacancy_div.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'}).text.strip() if vacancy_div.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'}) else ''
                experience = vacancy_div.find('span', {'data-qa': 'vacancy-serp__vacancy-experience'}).text.strip() if vacancy_div.find('span', {'data-qa': 'vacancy-serp__vacancy-experience'}) else ''
                location = vacancy_div.find('span', {'data-qa': 'vacancy-serp__vacancy-address'}).text.strip() if vacancy_div.find('span', {'data-qa': 'vacancy-serp__vacancy-address'}) else ''
                link = vacancy_div.find('a', {'data-qa': 'vacancy-serp__vacancy-title'})['href']

                # Save to database
                Vacancy.objects.create(
                    title=title,
                    employer=employer,
                    compensation=compensation,
                    experience=experience,
                    location=location,
                    link=link
                )
            self.stdout.write(self.style.SUCCESS('Successfully scraped and stored vacancies'))
        else:
            self.stdout.write(self.style.ERROR('Failed to retrieve the page'))
