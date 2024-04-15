from abc import ABC, abstractmethod


class AbstractApi(ABC):
    '''Абстрактный класс для создания классов поиска вакинсий с различных сайтов'''
    @abstractmethod
    def __init__(self):
         pass

    @abstractmethod
    def load_vacancies(self, keyword):
         pass
