import csv
import re
from datetime import datetime
import os
from statistics import mean
import openpyxl
from matplotlib import ticker
from openpyxl.styles import Font, Border, Side
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from jinja2 import Environment, FileSystemLoader
import pdfkit
import doctest
import cProfile as profile


def quick_quit(msg):
    """Осуществляет выход из программы с сообщением.

    Args:
          msg (str): Сообщение, которое нужно вывести
    """
    print(msg)
    exit(0)


class UserInput:
    """Класс для принятия вводимых значений.

    Attributes:
        file_name (string): Название файла
        vacancy_name (string): Название профессии
    """

    def __init__(self):
        """Инициализирует объект UserInput, принимает пользовательский ввод"""
        self.file_name = input('Введите название файла: ')
        self.vacancy_name = input('Введите название профессии: ')


class DataSet:
    """Класс для чтения и обработки данных файла с расширением .csv.

    Attributes:
        data (list[list[str]]): Список всех строк файла
        names (list[str]): Список с названиями колонок
        all_data (list[list[str]]): Список всех строк файла без учета строки с названиями колонок и строк,
         в которых есть пустые элементы
    """

    def __init__(self, file_name):
        """Инициализирует объект DataSet, выполняет чтение и обработку данных .csv файла

        Args:
            file_name (str): Название файла
        """
        if os.stat(file_name).st_size == 0:
            quick_quit("Пустой файл")

        self.data = [row for row in csv.reader(open(file_name, encoding="utf_8_sig"))]
        self.names = self.data[0]
        self.all_data = [row for row in self.data[1:] if len(row) == len(self.names) and row.count('') == 0]

        if len(self.all_data) == 0:
            quick_quit('Нет данных')


class Vacancy:
    """Класс для представления одной вакансии.

    Attributes:
        published_at (str): Дата публикации вакансии
    """

    published_at = []

    def __init__(self, all_data):
        for pers_data in all_data:
            for name, item in pers_data.items():
                if name == 'published_at':
                    self.published_at.append(self.get_year(item))

    @staticmethod
    def get_year(date):
        # new_data = int(datetime.strptime(date, '%Y-%m-%dT%H:%M:%S%z').strftime("%Y"))
        new_data = int(".".join(date[:4].split("-")))
        # big, small = date[:19].split('T')
        # year, month, day = big.split('-')
        # new_data = int(year)
        return new_data


def parse_html(info):
    info = re.sub('<.*?>', '', info)
    info = info.replace("\r\n", "\n")
    res = [' '.join(word.split()) for word in info.split('\n')]
    return res[0] if len(res) == 1 else res


inputed = UserInput()
dataset = DataSet(inputed.file_name)
(names, all_vac_data) = dataset.names, dataset.all_data

new_all_data = []
for data in all_vac_data:
    new_all_data.append(dict(zip(names, map(parse_html, data))))

parsed_data = Vacancy(new_all_data)
print(parsed_data.published_at)

profile.run('Vacancy(new_all_data)')
