import json
from json import JSONDecodeError

from src.vacancy_data_storage import VacancyDataStorage


class JSONVacancyDataStorage(VacancyDataStorage):
    """
    Класс для работы с json-файлом
    """
    def __init__(self, filename='vacancies.json'):
        self.filename = filename

    def add_vacancies(self, vacancies) -> None:
        """
        Записывает найденные вакансии в json-файл
        :param vacancies: список вакансий
        """
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(vacancies, file, ensure_ascii=False)

    def get_data_from_file(self) -> list:
        """
        Получает информацию о вакансиях из json-файла
        :return: возвращает список вакансий. Если файл пустой, то возвращает пустой список
        """
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                f = json.load(file)
                return f
        except JSONDecodeError:
            return []

    def remove_data_from_file(self) -> None:
        """
        Удаляет из json-файла данные о вакансиях
        """
        with open(self.filename, 'w', encoding='utf-8') as file:
            file.seek(0)
            file.truncate()
