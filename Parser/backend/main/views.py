from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Job, Anketa
from .parsers import parse_habr_vacancies, parse_habr_resumes

def index(request):
    vacancies_query = request.GET.get('vacancies_query', '')
    resumes_query = request.GET.get('resumes_query', 'python developer')

    if request.method == 'POST':
        vacancies_query = request.POST.get('vacancies_query', 'python')
        return HttpResponseRedirect(reverse('index') + f'?vacancies_query={vacancies_query}')


    vacancies_list = parse_habr_vacancies(vacancies_query)
    resumes_list = parse_habr_resumes(resumes_query)


    Job.objects.all().delete()
    Anketa.objects.all().delete()


    for vacancy_data in vacancies_list:
        Job.objects.create(
            title=vacancy_data['title'],
            company=vacancy_data['company'],
            location=vacancy_data['location'],
            salary=vacancy_data['salary'],
            link=vacancy_data['link'],
        )

    for resume_data in resumes_list:
        Anketa.objects.create(
            name=resume_data['name'],
            position=resume_data['position'],
            skills=resume_data['skills'],
            link=resume_data['link'],
        )

    context = {
        'vacancies': Job.objects.all(),
        'resumes': Anketa.objects.all(),
        'vacancies_query': vacancies_query,
    }

    return render(request, 'index.html', context)

