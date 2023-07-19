from src.json_vacancy_data_storage import JSONVacancyDataStorage
from src.vacancy import Vacancy


def displays_top_vacancies_by_salary() -> None:
    """Выводит топ N вакансий по зарплате"""
    while True:
        try:
            number_vacancies = int(input("Введите количество вакансий для вывода в топ N: "))
            break
        except ValueError:
            print("Не корректный ввод. Введите количество вакансий цифрами")
            continue
    vacancies_sort = Vacancy.sorts_the_list(Vacancy.all)
    if number_vacancies > len(Vacancy.all):
        number_vacancies = len(Vacancy.all)
    print(f"Топ {number_vacancies} вакансий по зарплате:")
    Vacancy.prints_a_formatted_list_vacancies(vacancies_sort, number_vacancies)


def filters_and_displays_vacancies() -> None:
    """Фильтрует вакансии по горду/зарплате и выводит результат пользователю"""
    team_number = input("Выберите параметры фильтрации вакансий: \n1 - город \n2 - зарплата\n")
    if team_number == "1":
        user_city = input("Введите название города\n")
        vacancies_city = Vacancy.filtering_vacancies_by_city(user_city)
        if vacancies_city:
            Vacancy.prints_a_formatted_list_vacancies(vacancies_city)
            user_input = input("Сохранить выбранные вакансии в файл\n1 - да\nEnter - нет\n")
            if user_input == "1":
                JSONVacancyDataStorage().add_vacancies(vacancies_city)
                print("Выбранные вакансии сохранены в файл")
        else:
            print("По вашему запросу ничего ненайдено")
    elif team_number == "2":
        while True:
            try:
                user_salary = int(input("Введите зарплату, от уровня которой необходимо показать вакансии\n"))
                break
            except ValueError:
                print("Не корректный ввод. Введите цифрами зарплату")
                continue
        vacancies_salary = Vacancy.filtering_vacancies_by_salary(user_salary)
        if vacancies_salary:
            Vacancy.prints_a_formatted_list_vacancies(vacancies_salary)
            user_input = input("Сохранить выбранные вакансии в файл\n1 - да\nEnter - нет\n")
            if user_input == "1":
                JSONVacancyDataStorage().add_vacancies(vacancies_salary)
                print("Выбранные вакансии сохранены в файл")
        else:
            print("По вашему запросу ничего ненайдено")
    else:
        print("Не корректный ввод")