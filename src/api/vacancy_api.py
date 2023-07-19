import json
import os
from abc import ABC, abstractmethod


import requests


class VacancyAPI(ABC):
    """
    Абстрактный класс, для работы с API сайтов с вакансиями
    """

    def __init__(self, url, count_vacancies=100):
        self._url = url
        self._count_vacancies = count_vacancies

    @abstractmethod
    def get_vacancies(self, job_title):
        pass
