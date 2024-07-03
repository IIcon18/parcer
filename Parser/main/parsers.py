import requests
from bs4 import BeautifulSoup
from .models import Job, Anketa

def parse_habr_vacancies(query):
    url = f'https://career.habr.com/vacancies?q={query}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    vacancies = []
    for card in soup.find_all('div', class_='vacancy-card__inner'):
        vac_company = card.find('a', class_="link-comp link-comp--appearance-dark").text.strip()
        vac_title = card.find('a', class_='vacancy-card__title-link').text.strip()
        vac_location = ', '.join([item.text.strip() for item in card.find_all('span', class_='preserve-line')])
        vac_salary = card.find('div', class_='vacancy-card__salary').text.strip() if card.find('div', class_='vacancy-card__salary') else 'Not specified'
        vac_link = 'https://career.habr.com' + card.find('a', class_='vacancy-card__title-link')['href']

        vacancies.append({
            'title': vac_title,
            'company': vac_company,
            'location': vac_location,
            'salary': vac_salary,
            'link': vac_link,
        })

    return vacancies

def parse_habr_resumes(query):
    url = f'https://career.habr.com/resumes?q={query}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    resumes = []
    for card in soup.find_all('div', class_="resume-card__body"):
        resume_name = card.find('a', class_="resume-card__title-link").text.strip()
        resume_position = card.find('div', class_="resume-card__specialization").text.strip()
        resume_skills = ', '.join([skill.text.strip() for skill in card.find_all('div', class_="content-section")])
        resume_link = 'https://career.habr.com' + card.find('a', class_='resume-card__title-link')['href']

        resumes.append({
            'name': resume_name,
            'position': resume_position,
            'skills': resume_skills,
            'link': resume_link,
        })

    return resumes
