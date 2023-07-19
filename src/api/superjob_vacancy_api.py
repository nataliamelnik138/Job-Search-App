import os

import requests

from src.api.vacancy_api import VacancyAPI

api_key = "v3.r.137682511.3c302dee126a971e14f5bb2cd5f462b27bfe1562.776ced6831e567301473c7b72d519dc1ed6d50ad"


class SuperJobVacancyAPI(VacancyAPI):
    """
    Класс, для работы с API сайта superjob.ru
    """
    url = 'https://api.superjob.ru/2.0/vacancies'

    def __init__(self, url=url):
        super().__init__(url)

    def get_vacancies(self, job_title) -> list:
        """
        Получает данные о вакансиях с сайта superjob.ru
        :param job_title: ключевое слово для поиска вакансий
        :return: список вакансий
        """
        params = {
            "keywords": [[1, job_title]],
            "count": self._count_vacancies,
        }

        headers = {
            "X-Api-App-Id": os.getenv('API_KEY_SUPERJOB')

        }
        response = requests.get(self.url, headers=headers, params=params)
        response_json = response.json()

        return response_json.get("objects", [])
