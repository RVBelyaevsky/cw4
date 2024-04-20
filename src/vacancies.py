class Vacancy:
    '''класс для создания экземпляра вакансии'''
    def __init__(self, name: str, url: str, salary: int, requirement: str):
        self.name = name
        self.url = url
        self.salary = self.cheking_salary(salary)
        self.requirement = self.checking(requirement)


    @classmethod
    def cast_to_object_list(cls, vacancies: list):
        """Метод для преобразования списка вакансий в список объектов"""
        vacancies_list = []
        for vacancy in vacancies:
            name = vacancy['name']
            url = vacancy['apply_alternate_url']
            salary = vacancy['salary']
            requirement = vacancy['snippet']['requirement']
            vacancies_list.append(cls(name, url, salary, requirement))
        return vacancies_list

    @staticmethod
    def checking(value):
        """Проверка на наличие значения в вакансии"""
        if value is None:
            return f"Работодатель не указал требований"
        else:
            return f"{value}"

    @staticmethod
    def cheking_salary(salary):
        """Проверка на нулевые значения зарплаты"""
        if isinstance(salary, dict):
            if salary['from'] is None:
                return int(salary['to'])
            elif salary['to'] is None:
                return int(salary['from'])
            else:
                return int(salary['to'])
        else:
            return 0

    def __lt__(self, other):
        return self.salary < other.salary

    def __repr__(self):
        return f'{self.__class__.__name__}. Атрибуты: {self.name}, {self.url}, {self.salary}, {self.requirement}'

    def __str__(self):
        return f'Должность: {self.name}\n Сайт: {self.url}\n Зарплата: {self.salary}\n Требования: {self.requirement}\n'