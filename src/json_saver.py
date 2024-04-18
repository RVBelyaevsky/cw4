from abc import ABC, abstractmethod


class AbstractSaver(ABC):
    """
    Абстрактный класс для определения методов класса работы с файлами
    """

    @abstractmethod
    def open_file(self):
        pass

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass


class JSONSaver(AbstractSaver):
    """
    Класс для работы с файлами
    """

    def open_file(self):
        pass

    def add_vacancy(self, vacancy):
        pass

    def delete_vacancy(self):
        pass
