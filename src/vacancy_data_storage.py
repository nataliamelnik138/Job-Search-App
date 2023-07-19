from abc import ABC, abstractmethod


class VacancyDataStorage(ABC):
    """
    Абстрактный класс для работы с файлом
    """
    @abstractmethod
    def add_vacancies(self, vacancy):
        pass

    @abstractmethod
    def get_data_from_file(self):
        pass

    @abstractmethod
    def remove_data_from_file(self):
        pass
