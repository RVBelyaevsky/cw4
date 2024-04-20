import json
import os
from abc import ABC, abstractmethod


class AbstractSaver(ABC):
    """
    Абстрактный класс для определения методов класса работы с файлами
    """

    @abstractmethod
    def __init__(self, file):
        pass

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

    def __init__(self, file_name):
        self.file_name = file_name

    def open_file(self):
        with open(self.file_name, 'r', encoding='UTF=8') as f:
            return json.load(f)

    def add_vacancy(self, vacancy):
        with open(self.file_name, 'w', encoding='UTF-8') as f:
            vac_json = []
            for vac in vacancy:
                vac_json.append(vac.__dict__)
            json.dump(vac_json, f, indent=4, ensure_ascii=False)

    def delete_vacancy(self):
        """Удаляем json файл"""
        os.remove(self.file_name)
