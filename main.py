from src.api.hh_vacancy_api import HHVacancyAPI
from src.api.superjob_vacancy_api import SuperJobVacancyAPI
from src.json_vacancy_data_storage import JSONVacancyDataStorage
from src.utils import displays_top_vacancies_by_salary, filters_and_displays_vacancies
from src.vacancy import Vacancy


def user_interaction():
    """Функция для взаимодействия с пользователем"""
    while True:
        servis_vacancies = input('Выберите платформу для поиска вакансий:\n1 - hh.ru\n'
                                 '2 - superjob.ru\n3 - hh.ru и superjob.ru\n')
        if servis_vacancies not in ["1", "2", "3"]:
            print("Не корректный ввод. Введите цифру, соответствующую номеру команды")
            continue
        else:
            break
    while True:
        job_title = input('Введите ключевое слово для поска вакансий\n')
        if not HHVacancyAPI().get_vacancies(job_title) or not SuperJobVacancyAPI().get_vacancies(job_title):
            print("По вашему запросу ничего не найдено. Измените параметры запроса")
            continue
        else:
            break
    if servis_vacancies == "1":
        website = "hh.ru"
        Vacancy.instance_from_list(job_title, 1)
    elif servis_vacancies == "2":
        website = "superjob.ru"
        Vacancy.instance_from_list(job_title, 2)
    elif servis_vacancies == "3":
        website = "hh.ru и superjob.ru"
        Vacancy.instance_from_list(job_title, 1)
        Vacancy.instance_from_list(job_title, 2)

    print(f'Вы выбрали для поиска вакансий {website}\nПо Вашему запросу "{job_title}" получены вакансии.')
    while True:
        user_input = input("Выберите дальнейшие действия:\n1 - Вывести на экран все найденные вакансии\n2 - Сохранить "
                           "вакансии в файл\n3 - Вывести топ N вакансий по зарплате\n4 - Ввести дополнительные данные "
                           "для фильтрации вакансий\n5 - Вывести информацию о вакансиях из файла\n6 - Удалить "
                           "информацию о вакансиях из файла\n7 - Новый поиск\n8 - Выход\n")
        if user_input == "1":
            Vacancy.prints_a_formatted_list_vacancies(Vacancy.all)
            continue
        elif user_input == "2":
            JSONVacancyDataStorage().add_vacancies(Vacancy.all)
            print("Вакансии сохранены в файл")
        elif user_input == "3":
            displays_top_vacancies_by_salary()
        elif user_input == "4":
            filters_and_displays_vacancies()
        elif user_input == "5":
            vacancies_from_file = JSONVacancyDataStorage().get_data_from_file()
            Vacancy.prints_a_formatted_list_vacancies(vacancies_from_file)
        elif user_input == "6":
            JSONVacancyDataStorage().remove_data_from_file()
            print("Информация о вакансиях из файла удалена")
        elif user_input == "7":
            user_interaction()
            break
        elif user_input == "8":
            print("Работа программы завершена! Всего доброго!")
            break
        else:
            print("Не корректный ввод")
            continue


if __name__ == "__main__":
    print("Добрый день!")
    user_interaction()
