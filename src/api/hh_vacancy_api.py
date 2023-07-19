import requests

from src.api.vacancy_api import VacancyAPI


class HHVacancyAPI(VacancyAPI):
    """
    Класс, для работы с API сайта hh.ru
    """
    url = 'https://api.hh.ru/vacancies'

    def __init__(self, url=url):
        super().__init__(url)

    def get_vacancies(self, job_title) -> list:
        """
        Получает данные о вакансиях с сайта hh.ru
        :param job_title: ключевое слово для поиска вакансий
        :return: список вакансий
        """
        params = {"text": job_title, "per_page": self._count_vacancies}

        response = requests.get(self.url, params=params)
        response_json = response.json()

        return response_json.get("items", [])
