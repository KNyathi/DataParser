# myapp/management/commands/extract_applicants.py
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import requests
from myapp.models import Applicant

class Command(BaseCommand):
    help = 'Scrape data from hh.ru'

    def handle(self, *args, **kwargs):
        url = "https://hh.ru/search/resume?text=python&area=1&isDefaultArea=true&exp_period=all_time&logic=normal&pos=full_text&hhtmFrom=vacancy_search_list&hhtmFromLabel=resume_search_line"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            for applicant_div in soup.find_all('div', {'data-qa': 'resume-serp__resume'}):
                title = applicant_div.find('a', {'data-qa': 'serp-item__title'}).text.strip()
                age = applicant_div.find('span', {'data-qa': 'resume-serp__resume-age'}).text.strip() if applicant_div.find('span', {'data-qa': 'resume-serp__resume-age'}) else ''
                experience_duration = applicant_div.find('div', {'data-qa': 'resume-serp__resume-excpirience-sum'}).text.strip() if applicant_div.find('div', {'data-qa': 'resume-serp__resume-excpirience-sum'}) else ''
                last_employer = applicant_div.find('div', {'data-qa': 'resume-serp_resume-item-content'}).text.strip() if applicant_div.find('div', {'data-qa': 'resume-serp_resume-item-content'}) else ''
                status = applicant_div.find('div', {'class': 'tag--vCYld4yoLU7RpJglYGnV tag_job-search-status-active--WAZ6Sx3vDygvcdzNm06h'}).text.strip() if applicant_div.find('div', {'class': 'tag--vCYld4yoLU7RpJglYGnV tag_job-search-status-active--WAZ6Sx3vDygvcdzNm06h'}) else ''
                link = applicant_div.find('a', {'data-qa': 'serp-item__title'})['href']
                last_position = applicant_div.find('div', {'data-qa': 'resume-serp_resume-item-content'}).text.strip() if applicant_div.find('div', {'data-qa': 'resume-serp_resume-item-content'}) else ''
                employment_dates = applicant_div.find('span', {'data-qa': 'resume-serp__resume-excpirience-sum'}).text.strip() if applicant_div.find('span', {'data-qa': 'resume-serp__resume-excpirience-sum'}) else ''

                # Save to database
                Applicant.objects.create(
                    title=title,
                    age=age,
                    experience_duration=experience_duration,
                    last_employer=last_employer,
                    status=status,
                    link=link,
                    last_position=last_position,
                    employment_dates=employment_dates
                )
            self.stdout.write(self.style.SUCCESS('Successfully scraped and stored applicants'))
        else:
            self.stdout.write(self.style.ERROR('Failed to retrieve the page'))
