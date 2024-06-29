# myapp/management/commands/extract_applicants.py

from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import requests
from myapp.models import Applicant

class Command(BaseCommand):
    help = 'Extract applicants and store them in the database'

    def handle(self, *args, **kwargs):
        url = 'https://hh.ru/search/resume?text=python&area=1&isDefaultArea=true&exp_period=all_time&logic=normal&pos=full_text&hhtmFrom=vacancy_search_list&hhtmFromLabel=resume_search_line'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        applicants = []

        for applicant in soup.select('[data-qa="resume-serp__resume"]'):
            title = applicant.select_one('h3 .serp-item__title').text.strip()
            link = applicant.select_one('h3 .serp-item__title a')['href']
            age = applicant.select_one('[data-qa="resume-serp__resume-age"]').text.strip()
            status = applicant.select_one('.tag_job-search-status-active--WAZ6Sx3vDygvcdzNm06h').text.strip()
            experience_duration = applicant.select_one('[data-qa="resume-serp__resume-excpirience-sum"]').text.strip()
            last_employer = applicant.select_one('.bloko-text_strong').text.strip()
            last_position = applicant.select_one('[data-qa="last-experience-link"]').text.strip()
            employment_dates = applicant.select_one('[data-qa="resume-serp_resume-item-content"] span:nth-of-type(2)').text.strip()

            applicants.append({
                'title': title,
                'link': link,
                'age': age,
                'status': status,
                'experience_duration': experience_duration,
                'last_employer': last_employer,
                'last_position': last_position,
                'employment_dates': employment_dates,
            })

        for applicant_data in applicants:
            Applicant.objects.update_or_create(
                link=applicant_data['link'],
                defaults=applicant_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully extracted and stored applicants'))
