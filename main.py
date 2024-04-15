from src.hh_api import HHApi
from src.vacancies import Vacancy

def main():
    hh = HHApi()
    hh_vacancies = hh.load_vacancies('водитель')
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    for i in vacancies_list:
        print(i.name)

if __name__ == "__main__":
    main()
