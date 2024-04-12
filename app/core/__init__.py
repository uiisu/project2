from abc import ABC, abstractmethod
from io import StringIO

import pandas


def convert_arabic_to_roman(number: int) -> str:
    """
    Функция конвертирует арабское число в римское.

    Args:
        number (int): Арабское число.

    Returns:
        roman (str): Римское число при успехе, иначе 'не поддерживается'.
    """
    roman_numbers = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                     'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                     'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    roman = ''
    if number in range(1, 3999):
        for key, value in roman_numbers.items():
            while number >= value:
                roman += key
                number -= value
        return roman
    else:
        return "не поддерживается"


def convert_roman_to_arabic(number: str) -> int:
    """
    Функция конвертирует римское число в арабское.

    Args:
        number (str): Римское число.

    Returns:
        arabic (str): Арабское число при успехе, иначе -1.
    """
    roman_numbers = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                     'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                     'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    arabic = 0
    flag = True
    for i in range(len(number)):
        if not flag:
            return -1
        flag = False
        for key, value in roman_numbers.items():
            if (i != len(number) - 1) and (key == number[i] + number[i + 1]) and (len(number) > 1):
                arabic += value
                i += 2
                flag = True
                break
            elif key == number[i]:
                arabic += value
                i += 1
                flag = True
                break
    return -1 if arabic == 0 else arabic


def average_age_by_position(file):
    """
    Функция принимает на вход CSV файл с данными о сотрудниках компании и
    возращает словарь со средним возрастом сотрудников на каждой должности.

    Args:
        file: CSV файл

    Returns:
        file: словарь в следующем формате : {"index": [<Уникальные должности>], "columns": [["Возраст","mean"]],
                                             "data": [[<Средний возраст для каждой должности соответственно>]]}
    """
    lines = [line.strip().split(",") for line in file.split(' ')]
    headers = lines.pop(0)
    dict_lines = [dict(zip(headers, row)) for row in lines]
    file = pandas.DataFrame(dict_lines)
    file['Возраст'] = file['Возраст'].astype('int')
    agg_func = {
        'Возраст': ['mean']
    }
    file = file.groupby(['Должность']).agg(agg_func)
    return file.to_dict(orient='split')


"""
Задание_6.
Дан класс DataGenerator, который имеет два метода: generate(), to_file()
Метод generate генерирует данные формата list[list[int, str, float]] и записывает результат в
переменную класса data
Метод to_file сохраняет значение переменной generated_data по пути path c помощью метода
write, классов JSONWritter, CSVWritter, YAMLWritter.

Допишите реализацию методов и классов.
"""


class BaseWriter(ABC):
    """Абстрактный класс с методом write для генерации файла"""

    @abstractmethod
    def write(self, data: list[list[int, str, float]]) -> StringIO:
        """
        Записывает данные в строковый объект файла StringIO
        :param data: полученные данные
        :return: Объект StringIO с данными из data
        """
        pass


class JSONWriter(BaseWriter):
    """Потомок BaseWriter с переопределением метода write для генерации файла в json формате"""

    """Ваша реализация"""

    pass


class CSVWriter:
    """Потомок BaseWriter с переопределением метода write для генерации файла в csv формате"""

    """Ваша реализация"""

    pass


class YAMLWriter:
    """Потомок BaseWriter с переопределением метода write для генерации файла в yaml формате"""

    """Ваша реализация"""

    pass


class DataGenerator:
    def __init__(self, data: list[list[int, str, float]] = None):
        self.data: list[list[int, str, float]] = data
        self.file_id = None

    def generate(self, matrix_size) -> None:
        """Генерирует матрицу данных заданного размера."""

        data: list[list[int, str, float]] = []
        """Ваша реализация"""

        self.data = data

    def to_file(self, path: str, writer) -> None:
        """
        Метод для записи в файл данных полученных после генерации.
        Если данных нет, то вызывается кастомный Exception.
        :param path: Путь куда требуется сохранить файл
        :param writer: Одна из реализаций классов потомков от BaseWriter
        """

        """Ваша реализация"""

        pass
