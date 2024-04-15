from abc import ABC, abstractmethod
import requests


class AbstractApi(ABC):
    '''Абстрактный класс для создания классов поиска вакинсий с различных сайтов'''
    @abstractmethod
    def __init__(self):
         pass

    @abstractmethod
    def load_vacancies(self, keyword):
         pass


class HHApi(AbstractApi):
    '''Класс для работы с Api сайта HeadHunter'''

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def load_vacancies(self, keyword):
        '''Функция возвращает список вакансий по ключевому слову пользователя'''

        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1

