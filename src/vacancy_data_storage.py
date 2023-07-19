from abc import ABC, abstractmethod


class VacancyDataStorage(ABC):
    """
    Абстрактный класс для работы с файлом
    """
    def add_vacancies(self, vacancy):
        pass

    def get_data_from_file(self):
        pass

    def remove_data_from_file(self):
        pass
