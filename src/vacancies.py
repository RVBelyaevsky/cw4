class Vacancy:

    def __init__(self, name):
        self.name = name

    @classmethod
    def cast_to_object_list(cls, vacancies):
        vacancies_list = []
        for vacancy in vacancies:
            name = vacancy['name']
            vacancies_list.append(cls(name))
        return vacancies_list
