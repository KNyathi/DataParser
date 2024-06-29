import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from myapp.models import Vacancy, Applicant

class Command(BaseCommand):
    help = 'Scrape data from hh.ru and store in the database'

    def handle(self, *args, **kwargs):
        url = 'https://hh.ru/search/vacancy?text=python&area=1'  # Example URL for searching Python jobs in Moscow
        response = requests.get(url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            vacancies = soup.find_all('div', class_='vacancy-serp-item')
            
            for vacancy in vacancies:
                # Extract vacancy details
                title = vacancy.find('a', class_='bloko-link').text.strip()
                company = vacancy.find('div', class_='vacancy-serp-item__meta-info-company').text.strip()
                description = vacancy.find('div', class_='g-user-content').text.strip()
                
                # Extract additional fields such as salary, region, required experience, work format, and skills
                salary_elem = vacancy.find('div', class_='vacancy-serp-item__sidebar')
                salary = salary_elem.text.strip() if salary_elem else 'Not specified'
                
                region = 'Moscow'  # Hardcoding for this example; you can parse it dynamically if available
                
                required_experience_elem = vacancy.find('div', class_='vacancy-serp-item__label')
                required_experience = required_experience_elem.text.strip() if required_experience_elem else 'Not specified'
                
                work_format = 'Full time'  # Default value; can be parsed dynamically if available
                
                skills = description  # Simplification; you might need to parse actual skills if available

                # Create or update the Vacancy object
                vacancy_obj, created = Vacancy.objects.update_or_create(
                    title=title,
                    company=company,
                    defaults={
                        'description': description,
                        'salary': salary,
                        'region': region,
                        'required_experience': required_experience,
                        'work_format': work_format,
                        'skills': skills,
                    }
                )
                
                # Example: Create or get an applicant linked to the vacancy
                applicant_data = {
                    'name': 'John',
                    'surname': 'Doe',
                    'age': 30,
                    'country_of_origin': 'USA',
                    'email': 'john.doe@example.com',
                    'telephone': '123456789',
                    'native_language': 'English',
                    'foreign_languages': 'Spanish, French',
                    'work_experience': 'Previous experience in Python development.',
                    'education': 'Bachelor of Computer Science',
                }
                
                applicant_obj, created = Applicant.objects.get_or_create(
                    email=applicant_data['email'],
                    defaults=applicant_data
                )
                
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created applicant: {applicant_obj.name}'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Applicant already exists: {applicant_obj.name}'))
                
                # Link the applicant to the vacancy
                vacancy_obj.applicants.add(applicant_obj)
                
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Linked applicant {applicant_obj.name} to vacancy {vacancy_obj.title}'))
                    
            self.stdout.write(self.style.SUCCESS('Successfully scraped and stored vacancies and applicants.'))
        else:
            self.stdout.write(self.style.ERROR('Failed to retrieve data from hh.ru'))
