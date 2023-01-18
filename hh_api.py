import requests
import pprint
import json


def get_info(text):
    DOMAIN = 'https://api.hh.ru/'
    url = f'{DOMAIN}vacancies'
    found_vac = str(text)
    gorod = '1384'
    params = {
        'text': found_vac,
        'experience': 'noExperience',
        'area': gorod
    }

    result = requests.get(url, params=params).json()
    count_pages = result['pages']
    count_vac = len(result['items'])
    print(f'Страниц: {count_pages}\nВсего вакансий: {count_vac}')
    # pprint.pprint(result)
    items = result['items']
    employers_city = []
    sites = []
    employers = []
    skills = []
    for item in result['items']:
        # for sk in item['area']['name']:
        city = item['area']['name']
        emp = item['employer']['name']
        try:
            sal = item['salary']['from']
        except Exception:
            sal = 'Не указана'
        employers_city.append(f'Город: {city} Фирма: {emp} Зарплата от: {sal}')
    return employers_city
