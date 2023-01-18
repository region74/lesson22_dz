import requests
import pprint
import json

text = 'Python'


def get_info(text):
    DOMAIN = 'https://api.hh.ru/'
    url = f'{DOMAIN}vacancies'
    found_vac = text
    gorod = '1384'
    params = {
        'text': found_vac,
        'experience': 'noExperience',
        'area': gorod
    }

    result = requests.get(url, params=params).json()
    pprint.pprint(result)
    count_pages = result['pages']
    count_vac = len(result['items'])
    items = result['items']
    employers_city = []
    sites = []
    employers = []
    skills = []
    for item in result['items']:
        city = item['area']['name']
        emp = item['employer']['name']
        name=item['name']
        link = item['alternate_url']
        try:
            sal = item['salary']['from']
        except Exception:
            sal = 'Не указана'
        employers_city.append(f'Город: {city} Фирма: {emp} ' f'Должность: {name} Зарплата от: {sal} ' f'Ссылка вакансии: {link}')
    return employers_city


result = get_info(text)
pprint.pprint(result)
