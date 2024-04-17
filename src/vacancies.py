class Vacancy:
    '''класс для создания экземпляра вакансии'''
    def __init__(self, name: str, url: str, salary: int):
        self.name = name
        self.url = url
        self.salary = salary

    @classmethod
    def cast_to_object_list(cls, vacancies):
        vacancies_list = []
        for vacancy in vacancies:
            name = vacancy['name']
            url = vacancy['apply_alternate_url']
            salary = vacancy['salary']
            vacancies_list.append(cls(name, url, salary))
        return vacancies_list
