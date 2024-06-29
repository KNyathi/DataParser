# Adjusted script with additional debugging output
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import requests
from myapp.models import Vacancy

class Command(BaseCommand):
    help = 'Scrape data from hh.ru for vacancies'

    def handle(self, *args, **kwargs):
        url = "https://hh.ru/search/vacancy?text=Python+%D1%81%D1%82%D0%B0%D0%B6%D0%B5%D1%80&from=suggest_post&salary=&ored_clusters=true&area=1&hhtmFrom=vacancy_search_list&hhtmFromLabel=vacancy_search_line"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            for vacancy_div in soup.find_all('div', {'class': 'vacancy-search-item__card'}):
                title_elem = vacancy_div.find('span', {'class': 'vacancy-name--c1Lay3KouCl7XasYakLk'})
                title = title_elem.text.strip() if title_elem else 'N/A'
                
                employer_elem = vacancy_div.find('span', {'class': 'company-info-text--vgvZouLtf8jwBmaD1xgp'})
                employer = employer_elem.text.strip() if employer_elem else 'N/A'
                
                compensation_elem = vacancy_div.find('div', {'class': 'compensation-labels--uUto71l5gcnhU2I8TZmz'})
                compensation = compensation_elem.text.strip() if compensation_elem else 'N/A'
                
                experience_elem = vacancy_div.find('span', {'class': 'label--rWRLMsbliNlu_OMkM_D3'})
                experience = experience_elem.text.strip() if experience_elem else 'N/A'
                
                location_elem = vacancy_div.find('span', {'class': 'fake-magritte-primary-text--Hdw8FvkOzzOcoR4xXWni'})
                location = location_elem.text.strip() if location_elem else 'N/A'
                
                link_elem = vacancy_div.find('a', {'class': 'bloko-link'})
                link = link_elem['href'] if link_elem else 'N/A'

                # Save to database
                Vacancy.objects.create(
                    title=title,
                    employer=employer,
                    compensation=compensation,
                    experience=experience,
                    location=location,
                    link=link
                )

                # Output for debugging
                self.stdout.write(self.style.SUCCESS(f'Title: {title}, Employer: {employer}, Compensation: {compensation}, Experience: {experience}, Location: {location}, Link: {link}'))
            
            self.stdout.write(self.style.SUCCESS('Successfully scraped and stored vacancies'))
        else:
            self.stdout.write(self.style.ERROR('Failed to retrieve the page'))

