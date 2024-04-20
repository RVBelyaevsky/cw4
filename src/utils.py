from src.hh_api import HHApi
from src.vacancies import Vacancy


def user_connector():
    user_request = input("Введите ключевое слово для запроса: ")
    user_number = input("Для получения топ N вакансий по зарплате, введите число N: ")

    hh = HHApi().load_vacancies(user_request)
    vacancy_list = Vacancy.cast_to_object_list(hh)
    top_vacancy_list = sorted(vacancy_list, reverse=True)
    result = []

    for vacancy in range(int(user_number)):
        result.append(top_vacancy_list[vacancy])
    return result
