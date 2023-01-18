import requests
import pprint
import json


def get_info(text):
    DOMAIN = 'https://api.hh.ru/'
    url = f'{DOMAIN}vacancies'
    found_vac = text
    gorod = '1384'
    params = {
        'text': found_vac,
        # 'experience': 'noExperience',
        'area': gorod
    }

    result = requests.get(url, params=params).json()
    offers_data = []

    for item in result['items']:
        city = item['area']['name']
        employer = item['employer']['name']
        position = item['name']
        link = item['alternate_url']
        try:
            salary = item['salary']['from']
        except Exception:
            salary = 'Не указана'
        offers_data.append(
            f'Город: {city} Фирма: {employer} ' f'Должность: {position} Зарплата от: {salary} ' f'Ссылка вакансии: {link}')
    return offers_data
