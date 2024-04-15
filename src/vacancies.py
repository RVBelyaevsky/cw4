class Vacancy:

    def __init__(self, name):
        self.name = name

    def cast_to_object_list(self, vacancies):
        vacancies_list = []
        for vacancy in vacancies:
            name = vacancy['name']
            vacancies_list.append(name)
